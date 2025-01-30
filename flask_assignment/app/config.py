import os

class Config:
    MONGO_URI = "mongodb://localhost:27017/imdb"
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
    UPLOAD_FOLDER = "uploads"
    BATCH_SIZE = 10000
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)