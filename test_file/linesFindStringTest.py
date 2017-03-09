# -*- coding: utf-8 -*-
import time
import sys

def tail(f):
    """
    读取文档中的每一行
    """
    f.seek(0, 2)  # 移动到EOF
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def grep(lines, searchchtext):
    """
    搜索查询字符串
    """
    for line in lines:
        if searchchtext in line: yield line

if __name__ == '__main__':
    # 输入参数 文件名 搜索的字符串
    print sys.argv
    if len(sys.argv) != 3:
        print "文件输入错误"
        raise SystemExit(1)
    wwwlog = tail(open(sys.argv[1]))
    pylines = grep(wwwlog, sys.argv[2])
    for line in pylines:
        print line
