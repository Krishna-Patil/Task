import os, time, ast
import pandas as pd
from app.extensions import mongo
from .config import Config
from app.celery_worker import celery

@celery.task
def process_csv(filepath):
    collection = mongo.db.movies
    start_time = time.time()
    
    chunk_size = Config.BATCH_SIZE
    
    for chunk in pd.read_csv(filepath, dtype={
        "vote_average": "float32",
        "budget": "float32",
        "revenue": "float32",
        "runtime": "int32",
        "vote_count": "int32",
        "production_company_id": "Int32",
        "genre_id": "Int32"
    }, chunksize=chunk_size):
        chunk = chunk.fillna({
            "title": "Unknown",
            "release_date": "Unknown",
            "original_language": "Unknown",
            "vote_average": 0.0,
            "budget": 0.0,
            "revenue": 0.0,
            "runtime": 0,
            "vote_count": 0,
            "production_company_id": 0,
            "genre_id": 0,
            "languages": "[]"
        })
        chunk["languages"] = chunk["languages"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])

        records = chunk.to_dict(orient="records")

        if records:
            collection.insert_many(records)

    os.remove(filepath)
    print(f"CSV processed in {time.time() - start_time} seconds")