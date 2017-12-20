# -*- coding: utf-8 -*-
'''装饰器学习
'''

def write_log(func):

	def infun(va, *args, **kwargs):
		print "这是装饰器内部函数的调用"
		print func.__name__, func.__doc__
		return func(va)

	return infun

@write_log
def aa(va):
	'''测试函数'''
	print va

def bb(va):
	'''测试函数'''
	print va

if __name__ == '__main__':
	aa(12)
	bb = write_log(bb(11))