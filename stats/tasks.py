from celery import shared_task
from notes.services import create_stat_notes
from users.services import create_stat_users

@shared_task
def create_statistic():
    create_stat_users()
    create_stat_notes("txt")
    create_stat_notes("py")
    create_stat_notes("cpp")
    create_stat_notes("txt", 100)
    create_stat_notes("py", 10)
    create_stat_notes("cpp", 3)
