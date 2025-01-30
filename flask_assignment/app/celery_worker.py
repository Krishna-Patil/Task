from celery import Celery
from app.config import Config

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
celery.conf.update(result_backend=Config.CELERY_RESULT_BACKEND)