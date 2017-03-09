# -*- coding: utf-8 -*-
import threading
import datetime
import time

threadLock = threading.Lock()


def makeOrderNum(strHead):
    """
    订单流水号生成
    订单编号： 前缀 + 年月日时分 + 流水号
    打开订单编号保存的文件，其中文件内不能为空至少要有一个单号
    订单编号格式如：YZ201702201614220002
    """
    threadLock.acquire()  # 加锁，防并发

    ORDERFILE = open("order.txt","r+")

    ORDERALL = ORDERFILE.readlines()
    # 读取之前订单序列最大流水号的订单
    lastOrderNum = ORDERALL[-1]
    newOrderTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # 获取该订单的最后四位流水号
    footerNum = lastOrderNum[-4:]

    newFooterNum = str(int(footerNum) + 1).zfill(4)  # 流水号+1 位数不足四位补足
    newOrderNum = strHead + newOrderTime + newFooterNum  # 拼接新的订单号
    try:
        ORDERFILE.write(newOrderNum)  # 将订单号写入
        ORDERFILE.write("\n")  # 以文档形式保存，需要换行
    except Exception as err:
        print err
    finally:
        ORDERFILE.close()
        threadLock.release()  # 解锁


if __name__ == '__main__':
    print "请输入订单前缀："
    strHead = raw_input()

    def test(strHead):
        for x in range(5):
            makeOrderNum(strHead)
            time.sleep(1)

    # 双线程测试， 模拟同一时间时，多订单生成
    t = threading.Thread(target=test, args=(strHead,))
    t.start()
    h = threading.Thread(target=test, args=(strHead,))
    h.start()
