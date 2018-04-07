## demo2 说明

- 这里演示了关于配置的使用，以及运行一个项目文件夹的例子

## 启动命令

在当前路径下执行以下命令启动任务：

```
celery -A celery_app worker --loglevel=info
```

然后重新打开窗口，

执行`client.py`脚本，它会发送两个异步任务到 Broker，在 Worker 的窗口我们可以看到输出

注意两个终端的输入信息：


## 补充的知识

### apply_async 常用的参数如下

- countdown：指定多少秒后执行任务
- eta (estimated time of arrival)：指定任务被调度的具体时间，参数类型是 datetime
- expires：任务过期时间，参数类型可以是 int，也可以是 datetime