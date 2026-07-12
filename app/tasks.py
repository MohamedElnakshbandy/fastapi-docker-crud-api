import time

from app.celery_app import celery_app


@celery_app.task
def slow_add(x: int, y: int):
    time.sleep(10)
    return x + y