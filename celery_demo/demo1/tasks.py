import time
from celery import Celery, Task

broker = 'amqp://'
backend = 'amqp://'

app = Celery('demo1', broker=broker, backend=backend)


class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('task done: {0}'.format(retval))
        return super(MyTask, self).on_success(retval, task_id, args, kwargs)


    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task fail, reason: {0}'.format(exc))
        return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)


@app.task(base=MyTask)
def add(x, y):
    time.sleep(5)  # 模拟耗时任务
    return x + y


@app.task(base=MyTask)
def raiseError():
    raise KeyError
    return None 