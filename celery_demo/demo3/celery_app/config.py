from datetime import timedelta
from celery.schedules import crontab

# Broker and Backend
# BROKER_URL = 'amqp://'
# CELERY_RESULT_BACKEND = 'amqp://'

BROKER_URL = 'mongodb://localhost:27017/mydb'
CELERY_RESULT_BACKEND = 'mongodb://localhost:27017/'
CELERY_MONGODB_BACKEND_SETTINGS = {
    'database': 'mydb',
    'taskmeta_collection': 'my_taskmeta_collection',
}

# Timezone
CELERY_TIMEZONE='Asia/Shanghai'    # 指定时区，不指定默认为 'UTC'
# CELERY_TIMEZONE='UTC'

# import
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2'
)

# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
         'task': 'celery_app.task1.add',
         'schedule': timedelta(seconds=30),       # 每 30 秒执行一次
         'args': (5, 8)                           # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=11, minute=30),   # 每天早上 11 点 30 分执行一次
        'args': (3, 7)                            # 任务函数参数
    }
}