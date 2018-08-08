from app import celery


@celery.task()
def add_together(a, b):
    with open('./aa.txt', 'ab+') as f:
        f.write('123455'.encode())
    return a + b
