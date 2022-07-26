import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "like_or_report.settings")

app = Celery("like_or_report")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
