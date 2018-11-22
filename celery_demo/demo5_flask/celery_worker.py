# encoding=utf8
from app import create_app
from extensions import celery  # noqa

app = create_app()
