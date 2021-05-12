from celery import shared_task
from .models import Link
@shared_task
def update():
    print("recived getting price")
