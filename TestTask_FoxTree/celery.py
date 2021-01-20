import os
from celery import Celery
from celery.schedules import crontab
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TestTask_FoxTree.settings")
django.setup()

app = Celery("TestTask_FoxTree")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "get_exchange_rates_every_hour": {
        "task": "aggregator.tasks.get_exchange_rates",
        "schedule": crontab(minute="*/1"),
    }
}
