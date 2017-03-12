# -*- coding: utf-8 -*-
'''
责任链模式
'''


class Event:
    def __inin__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = 'handle_{}'.format(event)
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handler(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)
