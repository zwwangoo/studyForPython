from flask import Flask
from datetime import timedelta
from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend='redis://localhost:6379/0',
        broker='redis://localhost:6379',
        include=['task']
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask

    return celery


CELERYBEAT_SCHEDULE = {
    'aa': {
        'task': 'task.add_together',
        'args': (1, 2),
        'schedule': timedelta(seconds=5)
    }
}

app = Flask(__name__)
app.config.update(
    CELERYBEAT_SCHEDULE=CELERYBEAT_SCHEDULE,
)

celery = make_celery(app)
