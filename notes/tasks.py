from celery import shared_task
from .services import upload_csv_from_file



@shared_task
def upload_csv(file_csv,user):
    upload_csv_from_file(file_csv,user)