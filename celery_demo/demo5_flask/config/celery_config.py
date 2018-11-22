# encoding=utf8
from datetime import timedelta


class CeleryConfig(object):
    # celery default config
    CELERY_BROKER_URL = 'redis://localhost:16379/2'
    CELERY_RESULT_BACKEND = 'redis://localhost:16379/3'

    CELERYBEAT_SCHEDULE = {
        'sub': {
            'task': 'proj.tasks.sub',
            'args': (3, 2),
            'schedule': timedelta(seconds=5)
        }
    }
