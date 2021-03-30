from celery import shared_task
from notes.services import create_stat_notes
from users.services import create_stat_users

@shared_task
def create_statistic():
    create_stat_users()
    create_stat_notes()
    create_stat_notes(3)
