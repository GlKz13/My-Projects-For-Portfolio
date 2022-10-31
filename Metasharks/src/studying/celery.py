from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'University_api.settings')

app = Celery('University_api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()