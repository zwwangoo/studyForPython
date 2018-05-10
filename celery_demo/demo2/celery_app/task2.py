import time
from .celery import app


@app.task
def multiply(x, y):
    time.sleep(2)
    return x * y
