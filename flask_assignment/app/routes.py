import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.tasks import process_csv
from app.config import Config
from app.extensions import mongo

main_bp = Blueprint("main", __name__)

@main_bp.route('/upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Trigger Celery task
    process_csv.delay(filepath)

    return jsonify({"message": "File uploaded and processing started."}), 200

@main_bp.route('/movies', methods=['GET'])
def get_movies():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    language = request.args.get('language')
    sort_by = request.args.get('sort_by', 'release_date')
    order = int(request.args.get('order', 1))

    query = {}
    if language:
        query["language"] = language

    movies = mongo.db.movies.find(query).sort(sort_by, order).skip((page - 1) * per_page).limit(per_page)
    
    return jsonify([{**movie, "_id": str(movie["_id"])} for movie in movies])
