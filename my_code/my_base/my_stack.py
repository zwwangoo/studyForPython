class Stack:
    def __init__(self):
        self.value = []

    def push(self, value):
        self.value.append(value)

    def pop(self):
        if self.empty():
            raise Exception("Your stack is empty")
        return self.value.pop()

    def peek(self):
        if self.empty():
            raise Exception("Your stack is empty")
        return self.value[-1]

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.value)
