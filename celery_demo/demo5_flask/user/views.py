# encoding=utf8
import time
from datetime import datetime, timedelta
from flask import Blueprint
from proj.tasks import sum
from proj.delay import add

user = Blueprint('user', __name__)
task_id = ''


def utc_time_from_localtime_str():
    eta = datetime.now() + timedelta(seconds=12)
    unix_time = time.mktime(eta.timetuple())
    return datetime.utcfromtimestamp(unix_time)


@user.route('/')
def index():
    return 'ok'


@user.route('/tasks/post', methods=['GET'])
def tasks_list():
    # 10s之后执行该任务, countdown 倒计时,单位秒
    t1 = add.apply_async([1, 2], countdown=10)
    # 12秒之后执行该任务， 指定任务执行时间，类型为datetime时间类型
    t2 = sum.apply_async([1, 4], eta=utc_time_from_localtime_str())
    global task_id
    task_id = t1.task_id
    return 't1: {} <br> t2: {}'.format(t1.task_id, t2.task_id)


@user.route('/tasks/delete', methods=['GET'])
def tasks_delete():
    global task_id
    add.AsyncResult(task_id).revoke(terminate=True, signal='SIGKILL')
    return '1'
