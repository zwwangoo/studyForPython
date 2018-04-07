## demo1 说明

- 这里演示了celery的基本使用和增加任务完成和任务失败的重写

## 启动命令

在当前路径下执行以下命令启动任务：


```
celery worker -A tasks --loglevel=info
```

然后重新打开窗口，

执行`test.py`脚本

注意两个终端的输入信息：

---