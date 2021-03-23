from celery import shared_task
from .services import create_report

@shared_task()
def create_report_task(user_ids = None):
    create_report(user_ids)