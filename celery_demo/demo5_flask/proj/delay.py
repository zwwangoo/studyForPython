# encoding=utf8
from extensions import celery


@celery.task()
def add(a, b):
    print(a + b)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    return a + b
