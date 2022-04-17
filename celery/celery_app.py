import os
import time

from celery import Celery


# Initialize Celery
celery = Celery(
    'worker',
    broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379"),
    backend=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379"),
)


@celery.task()
def task1(arg):
    time.sleep(int(arg) * 10)
    return
