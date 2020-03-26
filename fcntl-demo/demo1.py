import fcntl


class Lock(object):

    def __init__(self, filename):
        self.filename = filename
        self.handle = open(filename, 'w')

    def acquice(self):
        fcntl.lockf(self.handle, fcntl.LOCK_EX)

    def release(self):
        fcntl.lockf(self.handle, fcntl.LOCK_UN)

    def __del__(self):
        self.handle.close()


try:
    lock = Lock('.lock')
    lock.acquice()
finally:
    lock.release()
