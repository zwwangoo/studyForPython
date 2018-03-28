from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://localhost/')
app.config_from_object('config')

@app.task
def add(x, y):
    return x + y
