#coding:utf-8
import thread
import time
import httplib
import random
import pp
import sys
import uuid
HOST = "10.55.91.107"  # 主机地址 例如192.168.1.101
PORT = 80  # 端口
URI = "/?" # 相对地址,加参数防止缓存，否则可能会返回304
TOTAL = 1  # 总数
SUCC = 0  # 响应成功数
FAIL = 0  # 响应失败数
EXCEPT = 0  # 响应异常数
MAXTIME = 0  # 最大响应时间
MINTIME = 1000  # 最小响应时间，初始值为100秒
GT3 = 0  # 统计3秒内响应的
LT3 = 0  # 统计大于3秒响应的


THREAD_NUMBER = 1000 # 并发的线程数


def test_performace():
    global TOTAL
    global SUCC
    global FAIL
    global EXCEPT
    global GT3
    global LT3
    global MAXTIME
    global MINTIME
    try:
        st = time.time()
        conn = httplib.HTTPConnection(HOST, PORT, False)
        conn.request('GET', URI + str(random.randint(100, 999)))
        res = conn.getresponse()
        # print 'version:', res.version
        # print 'reason:', res.reason
        print 'status:', res.status
        # print 'msg:', res.msg
        # print 'headers:', res.getheaders()
        if res.status == 200:
            TOTAL += 1
            SUCC += 1
        else:
            TOTAL += 1
            FAIL += 1
        time_span = time.time() - st
        if time_span < MINTIME:
            MINTIME = time_span
        # print 'used time = ',time_span
        # print 'MINTIME = ' , MINTIME
        if time_span > MAXTIME:
            MAXTIME = time_span
        # print 'MAXTIME = ', MAXTIME
        if time_span > 3:
            GT3 += 1
        else:
            LT3 += 1
    except Exception, e:
        print e
        TOTAL += 1
        EXCEPT += 1
    conn.close()
if __name__ == "__main__":
    start_time = time.time()
    print "==================================初始化多核心利用================================"
    ppservers = ()
    if len(sys.argv) > 1:
        ncpus = int(sys.argv[1])
        # Creates jobserver with ncpus workers
        job_server = pp.Server(ncpus, ppservers=ppservers)
    else:
        # Creates jobserver with automatically detected number of workers
        job_server = pp.Server(ppservers=ppservers)
    workers = job_server.get_ncpus()
    print "Starting pp with", workers, "workers"

    #
    def procton_collision(times):
        for i in range(int(times)):
            thread.start_new(test_performace, ())
    print "=================================开始任务========================================="
    jobs = [(job_server.submit(procton_collision, (THREAD_NUMBER/workers,), (test_performace,), ("uuid", "time", "httplib", "thread", )))for i in range(workers)]
    for job in jobs:
        job()
        job_server.print_stats()


    while TOTAL < 10:
        print TOTAL
        print "total:%d,succ:%d,fail:%d,except:%d\n" % (TOTAL, SUCC, FAIL, EXCEPT)
        print HOST, URI
        time.sleep(1)
print "=============================================TESK END============================="
print "used time ", time.time() - start_time
print "total:%d,succ:%d,fail:%d,except:%d" % (TOTAL, SUCC, FAIL, EXCEPT)
print 'response maxtime:', MAXTIME
print 'response mintime', MINTIME
print 'great than 3 seconds:%d,percent:%0.2f' % (GT3, float(GT3) / TOTAL)
print 'less than 3 seconds:%d,percent:%0.2f' % (LT3, float(LT3) / TOTAL)
