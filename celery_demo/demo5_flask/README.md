关于 Flask 与 Celery 的配合使用。

demo 演示了在 Flask 中如何使用 Celery 可以避免循环引用的问题。

演示的要点：

- celery 在 flask 中的使用
- celery 的定时任务
- celery 的异步任务
- celery 任务的web展示
- celery 任务的撤回

# 环境搭建

	pip install -r requirements.txt


# 启动Celery Worker


启动 Celery Worker 进程

	celery -A celery_worker.celery --loglevel=info worker

启动 Celery Beat 进程，定时将任务发送到 Broker

	celery beat -A celery_worker.celery -s ./proj/schedule/beat

一个终端启动

	celery -B -A celery_worker.celery worker --loglevel=info -s ./proj/schedule/beat


# 启动Flask

	python wsgi.py


打开浏览器：

执行异步定时任务：

[http://127.0.0.1:5000/user/tasks/post](http://127.0.0.1:5000/user/tasks/post)
