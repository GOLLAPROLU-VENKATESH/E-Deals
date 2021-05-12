import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ec3.settings')

app = Celery('ec3')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.beat_schedule={
#     'update_10_sec':{
#         'task':'price_tracker.tasks.update',
#         'schedule':60,
#     }
# }
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')