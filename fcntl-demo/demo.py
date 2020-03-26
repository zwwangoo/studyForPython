import fcntl
import time

# 在给文件加锁之前,一定要保证文件以相应的访问模式打开,
# 例如要对一个文件加上共享锁,一定要首先按读模式打开文件,
# 若要给文件加上排他锁,则首先要按写模式打开对应文件；若想加两种锁，则需要按读写模式打开.
f = open('.lock', 'wb')


def acquire():

    # LOCK_SH：表示要创建一个共享锁，在任意时间内，一个文件的共享锁可以被多个进程拥有；
    # LOCK_EX：表示创建一个排他锁，在任意时间内，一个文件的排他锁只能被一个进程拥有；
    # LOCK_UN：表示删除该进程创建的锁；
    # LOCK_MAND：它主要是用于共享模式强制锁，它可以与 LOCK_READ 或者 LOCK_WRITE联合起来
    # 使用，从而表示是否允许并发的读操作或者并发的写操作；

    fcntl.lockf(f, fcntl.LOCK_EX)
    return True


def release():
    # 1. 对于文件的 close() 操作会使文件锁失效；
    # 2. 同理，进程结束后文件锁失效
    # f.close()
    fcntl.lockf(f, fcntl.LOCK_UN)


for i in range(10):
    acquire()
    print(i)
    time.sleep(1)
    release()
