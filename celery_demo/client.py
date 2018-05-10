from celery_demo.demo2.celery_app.task1 import add


def test():
    t = add.apply_async(args=(2, 3), countdown=5)
    if t.status is 'PENDING':
        print("任务已经派送出去，请等待！")
    return 'Success'


if __name__ == "__main__":
    test()

