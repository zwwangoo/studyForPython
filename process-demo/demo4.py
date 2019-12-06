from multiprocessing import Process


class MyProcess(Process):

    def run(self):
        """
        实现 Process 启动的时候执行的任务
        """
        print('called run method in process: %s' % self.name)
        return


if __name__ == '__main__':
    p = MyProcess()
    p.start()
