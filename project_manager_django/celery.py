import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_manager_django.settings')
app = Celery('project_manager_django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()