from datetime import timedelta
from celery.schedules import crontab

# Broker and Backend
BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'amqp://'

# Timezone
CELERY_TIMEZONE='Asia/Shanghai'    # 指定时区，不指定默认为 'UTC'
# CELERY_TIMEZONE='UTC'

# import
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2'
)