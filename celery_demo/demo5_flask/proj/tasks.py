# encoding=utf8
from extensions import celery


@celery.task()
def sum(a, b):
    print(a * b)
    print('******************************************************')
    return a * b


@celery.task()
def sub(a, b):
    print(a - b)
    print('------------------------------------------------------')
    return a - b
