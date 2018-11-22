# encoding=utf8
from celery import Celery

celery = Celery('demo5_flask', include=['proj.tasks'])
