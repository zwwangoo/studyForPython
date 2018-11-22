# encoding=utf8
import os
from flask import Flask

from extensions import celery
from config.celery_config import CeleryConfig
from user.views import user

_default_instance_path = '%(instance_path)s/instance' % \
    {'instance_path': os.path.dirname(os.path.realpath(__file__))}


def create_app(instance_path=_default_instance_path):
    app = Flask(__name__, instance_relative_config=True,
                instance_path=instance_path)
    configure_app(app)
    configure_celery(app)
    configure_blueprint(app)
    return app


def configure_app(app, external_config=None):
    # celery default configs
    app.config.from_object(CeleryConfig)


def configure_celery(app):

    app.config.update({
        'BROKER_URL': app.config['CELERY_BROKER_URL'],
        'RESULT_BACKEND': app.config['CELERY_RESULT_BACKEND']
    })
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask


def configure_blueprint(app):
    app.register_blueprint(user, url_prefix='/user')
