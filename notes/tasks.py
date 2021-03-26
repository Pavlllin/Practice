from celery import shared_task
from .services import upload_csv_from_file



@shared_task
def upload_csv(path,user):
    upload_csv_from_file(path,user)