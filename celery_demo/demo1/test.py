import time
from .tasks import add, raiseError

re = add.delay(2, 2)

print('这里不会等待')

while not re.ready():
    time.sleep(1)

print('task done: {0}'.format(re.get()))

err = raiseError.delay()

print(err.status)