# -*- coding: utf-8 -*-
import os
import sys


class loginError(Exception):
    def __init__(self, value):
        self.value = value


def test(va):
    try:
        if va == 1:
            raise loginError("发生异常！")
        else:
            print "正常执行，没有异常发生"
    except loginError, err:
        print err.value
    except Exception, err:
        print err
    else:
        print 12


if __name__ == "__main__":
    test(0)
