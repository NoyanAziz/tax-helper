import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tax_helper.settings')

BROKER_HOST = os.environ.get('BROKER_HOST', None)
if BROKER_HOST is None:
    raise Exception("BROKER_HOST environmental variable is not defined")

broker_url = 'redis://' + BROKER_HOST + '/0'
app = Celery('tax_helper', broker=broker_url)


# app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """Debug task"""
    print(f'Request: {self.request!r}')
