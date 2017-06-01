# -*- coding: utf-8 -*-
import threading
import sys
import time
import httplib

HOST = '127.0.0.1'  # 主机
PORT = '8069'  # 服务端口
URI = '/?365'  # 对地址,加参数防止缓存，否则可能会返回304
THREAD = []
TOTAL = SUCCESS = FILL = EXCE =0
GT3 = LT3 = 0

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global TOTAL, SUCCESS, FILL, EXCE, GT3, LT3
        print "run name={}, Host='{}:{}' ".format(self.name, HOST, PORT)
        TOTAL += 1
        this_begin = time.time()
        try:
            conn = httplib.HTTPConnection(HOST, PORT, False)
            conn.request('GET', URI)
            res = conn.getresponse()
            spen_time = time.time() - this_begin
            if spen_time > 3:
                GT3 += 1
            else:
                LT3 += 1
            print "run name={}, Host='{}:{}', status={}".format(self.name, HOST, PORT, res.status)
            if res.status == 200:
                SUCCESS += 1
            else:
                FILL += 1
        except Exception as err:
            EXCE += 1
        conn.close()


def main():
    thread_count = 1000  # 并发量
    start_time = time.time()
    for i in range(thread_count):
        th = MyThread("Thread" + str(i))
        th.start()
        THREAD.append(th)

    for th in THREAD:
        th.join()
    end_time = time.time()
    continue_time = end_time - start_time
    print "Thread End! Total: {}, Success: {}, Fill: {}, Exec: {}".format(TOTAL, SUCCESS, FILL, EXCE)
    print "great than 3 seconds: {}, %: {}".format(GT3, GT3 / TOTAL)
    print "continue time: {}".format(continue_time)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        HOST, PORT = sys.argv[1].split(":")
    main()
