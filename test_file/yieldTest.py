# -*- coding: utf-8 -*-
"""
用生成器实现对文件最后一行增加的字符进行监控
这是测试，并不能做到监控在文件的何处做了增删
仅做到了对最后一行的增加字符的监控
"""
import time
import sys


def showTime(filename):
    testFile = open(filename)
    print filename
    testFile.seek(0,2)
    while True:
        line = testFile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    if len(sys.argv) != 2:  # 命令行输入监控文件的名字
        print "文件不存在"
        raise SystemExit(1)
    for i in showTime(sys.argv[1]):
        print i
