随便记录一下：：

添加任务，返回`AsyncResult`对象
`AsyncResult`对象除了get方法用于常用获取结果方法外还提以下常用方法或属性：

- `state`: 返回任务状态；
- `task_id`: 返回任务id；
- `get()`: 返回任务结果
- `result`: 返回任务结果，同get()方法；
- `ready()`: 判断任务是否以及有结果，有结果为True，否则False；
- `info()`: 获取任务信息，默认为结果；
- `wait(t)`: 等待t秒后获取结果，若任务执行完毕，则不等待直接获取结果，若任务在执行中，则wait期间一直阻塞，直到超时报错；
- `successfu()`: 判断任务是否成功，成功为True，否则为False；

Celery的提供的定时任务主要靠schedules来完成，通过beat组件周期性将任务发送给woker执行

`apply_async`支持常用参数：

- `eta`：指定任务执行时间，类型为datetime时间类型；
- `countdown`：倒计时,单位秒，浮点类型；
- `expires`：任务过期时间，如果任务在超过过期时间还未执行则回收任务，浮点类型获取datetime类型；
- `retry`：任务执行失败时候是否尝试，布尔类型。；
- `serializer`：序列化方案，支持pickle、json、yaml、msgpack；
- `priority`：任务优先级，有0～9优先级可设置，int类型；
- `retry_policy`：任务重试机制，其中包含几个重试参数，类型是dict如下：
