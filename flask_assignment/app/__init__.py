from flask import Flask
from app.config import Config
from app.extensions import mongo
from celery import Celery
from app.routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    app.register_blueprint(main_bp)

    return app

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    return celery

flask_app = create_app()
celery = make_celery(flask_app)