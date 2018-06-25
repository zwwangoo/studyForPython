# -*- coding: utf-8 -*-
class Stack(object):
    def __init__(self):
        self.stackData = []

    def push(self, item):
        return self.stackData.append(item)

    def pop(self):
        if self.isEmpoty():
            raise Exception("Your stack is empty！")
        return self.stackData.pop()

    def peek(self):
        if not self.isEmpoty():
            return self.stackData[0]

    def isEmpoty(self):
        return self.size() == 0

    def size(self):
        return len(self.stackData)


class MyStack(object):
    def __init__(self):
        self.stackData = Stack()
        self.stackMin = Stack()

    def push(self, newItem):
        if self.stackMin.isEmpoty():
            self.stackMin.push(newItem)
        elif newItem <= self.stackMin.peek():
            self.stackMin.push(newItem)
        self.stackData.push(newItem)

    def pop(self):
        value = self.stackData.pop()
        if value == self.stackMin.peek():
            self.stackMin.pop()
        return value
    def peek(self):
        if self.stackMin.isEmpoty():
            raise Exception("you stack is empty!")
        return self.stackMin.peek()


def main():
    my = MyStack()
    my.push(3)
    my.push(4)
    my.push(5)
    my.push(1)
    my.push(2)
    my.push(1)
    for i in range(5):
        print my.pop()
        print my.peek()

if __name__ == '__main__':
    main()
