# -*- coding: utf-8 -*-
'''
外观模式 2017-3-8
'''
from abc import ABCMeta, abstractmethod
''' python本身不提供抽象类和接口机制，要想实现抽象类，
    可以借助abc模块，ABC是Abstract Base Class的缩写
'''


class State:
    ''' 在python3.4以上可以使用枚举替换 '''
    new = 1
    running = 2
    sleeping = 3
    restart = 4
    zombie = 5


class User:
    pass


class Process:
    pass


class File:
    pass


class Server:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        ''' @abstractmethod装饰器来声明Server的所有子类都应实现（强制性）哪些方法 '''
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    def __init__(self):
        ''' 初始化文件服务进程要求的操作 '''
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print('booting the {}'.format(self))
        ''' 启动文件服务进程要求的操作 '''
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        ''' 终止文件服务进程的要求 '''
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        ''' 检查访问权限的有效性和用户权限等 '''
        print('trying to create the file {} for user {} with permissions {}'
              .format(name, user, permissions))


class ProcessServer(Server):
    def __init__(self):
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        print 'booting the {}'.format(self)

    def kill(self, restart=True):
        print 'Killing {}'.format(self)
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        ''' 检查用户权限和生成PID等 '''
        print 'trying to  create the process {} for user {}'.format(name, user)


class OperatingSystem:
    ''' 外观 '''
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file('foo', 'hello', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')


if __name__ == '__main__':
    main()