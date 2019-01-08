from ..my_base.my_stack import Stack


# ----------------------------------------------------------------
# ----------------------------------------------------------------


class MyStack:
    """
    2019-01-08
    实现一个有get_min功能的栈
    ---
    实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作
    1 pop,push, get_min操作的时间复杂度都是O(1)
    2 设计的站类型可以使用现成的栈结构
    """
    def __init__(self):
        self.stack_data = Stack()
        self.stack_min = Stack()

    def push(self, value):
        if self.stack_min.empty() or value <= self.get_min():
            self.stack_min.push(value)
        else:
            self.stack_min.push(self.get_min())

        self.stack_data.push(value)

    def pop(self):
        if self.stack_data.empty():
            raise
        self.stack_min.pop()
        return self.stack_data.pop()

    def get_min(self):
        if self.stack_min.empty():
            raise
        else:
            return self.stack_min.peek()


# ----------------------------------------------------------------
# ----------------------------------------------------------------


class TwoStacksQueue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def add(self, value):
        self.push_stack.push(value)

    def poll(self):
        if self.push_stack.empty() and self.pop_stack.empty():
            raise RuntimeError('Queue is empty')
        else:
            if self.pop_stack.empty():
                while not self.push_stack.empty():
                    self.pop_stack.push(self.push_stack.pop())
            return self.pop_stack.pop()

    def peek(self):
        if self.push_stack.empty() and self.pop_stack.empty():
            raise RuntimeError('Queue is empty')
        else:
            if self.pop_stack.empty():
                while not self.push_stack.empty():
                    self.pop_stack.push(self.push_stack.pop())
            return self.pop_stack.peek()
