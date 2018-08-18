from django.conf import settings
from celery import Celery

app = Celery('celery_talk', broker=settings.BROKER_URL)

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
