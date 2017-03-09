# -*- coding: utf-8 -*-
'''
该测试输出
__new__
<type 'NoneType'>
__init__
<type 'instance'>
''''''
在3.x里object已经做为所有东西的基类了
http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html
2017-3-10
'''

class A(object):
	def __init__(self):
		print '__init__'

	def __new__(cls):
		print '__new__'

class B:
	def __init__(self):
		print '__init__'

	def __new__(cls):
		print '__new__'

a = A()
print type(a)
b = B()
print type(b)