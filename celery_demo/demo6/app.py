from flask import Flask
from celery import Celery


def make_celery(app):
    celery = Celery('app')
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):

        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


app = Flask(__name__)
app.config.update(
    BROKER_URL='redis://localhost:16379/0',
)
celery = make_celery(app)


@celery.task()
def add_together(a, b):
    return a + b


@app.route('/')
def index():
    add_together.delay(1, 2)
    return 'ok'


if __name__ == '__main__':
    print(app.import_name)
    app.run()
