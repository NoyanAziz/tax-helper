import os
from celery import Celery


BROKER_HOST = os.environ.get('BROKER_HOST', None)
if BROKER_HOST is None:
    raise Exception("BROKER_HOST environmental variable is not defined")
broker_url = 'pyamqp://guest@' + BROKER_HOST + '//'

app = Celery('tasks', broker=broker_url, backend='rpc://')


@app.task
def add(x, y):
    return x + y
