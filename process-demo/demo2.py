import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print('Starting %s' % name)
    time.sleep(3)
    print('Exiting %s' % name)


if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name='foo_process', target=foo)
    # 为了在后台运行进程，我们设置 daemon 参数为 True
    # 后台运行进程在主进程结束之后会自动结束。
    # process_with_name.daemon = True
    process_with_default_name = multiprocessing.Process(target=foo)
    process_with_name.start()
    process_with_default_name.start()
