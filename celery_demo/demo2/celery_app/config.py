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