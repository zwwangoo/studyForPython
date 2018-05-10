from datetime import datetime, timedelta

from .celery_app import task1, task2

task1.add.apply_async(args=(1, 2))
task2.multiply.apply_async(args=[2, 3])

print('====ok====')

print('----下面演示5秒后执行任务，注意 worker 的输出----')

task1.add.apply_async(args=(2, 3), countdown=5)

task2.multiply.apply_async(args=(3, 7), eta=datetime.utcnow() + timedelta(seconds=10))