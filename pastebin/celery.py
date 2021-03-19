import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pastebin.settings')

app = Celery('pastebin')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'users.tasks.create_report',
        'schedule': crontab(hour=12, minute=31),
    },
}


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()