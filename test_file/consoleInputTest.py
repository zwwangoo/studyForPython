# -*- coding: utf-8 -*-
import sys

if len(sys.argv) != 2:
    print "文件名错误"
    raise SystemExit(1)

f = open(sys.argv[1])
lines = f.readlines()
f.close()

fvalues = [float(line) for line in lines]
print "最小数为：", min(fvalues)
print "最大数为：", max(fvalues)
