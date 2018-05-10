## demo3 说明

- 本 demo 演示了定时任务的创建和执行

## 启动命令

启动 Celery Worker 进程，在项目的根目录下执行下面命令：

```
celery -A celery_app worker --loglevel=info
```

接着，启动 Celery Beat 进程，定时将任务发送到 Broker，新打开终端，在项目根目录下执行下面命令：

```
celery beat -A celery_app
```

之后，在 Worker 窗口我们可以看到，任务 task1 每 30 秒执行一次，而 task2 每天早上 9 点 50 分执行一次。

在上面，我们用两个命令启动了 Worker 进程和 Beat 进程，我们也可以将它们放在一个命令中：

```
celery -B -A celery_app worker --loglevel=info
```

[参考](http://geek.csdn.net/news/detail/128791)