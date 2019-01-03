class MyStack(object):
    def __init__(self):
        self.values = []

    def size(self):
        return len(self.values)

    def empty(self):
        return self.size() == 0

    def push(self, value):
        self.values.append(value)

    def peek(self):
        if self.size() != 0:
            return self.values[-1]

    def pop(self):
        if self.size() != 0:
            return self.values.pop()


def csv2json(file_path):
    with open(file_path, 'rb+') as f:
        readlines = f.readlines()
        notes_stack = MyStack()
        root_stack = MyStack()

        for line in readlines:
            for index, value in enumerate(line.decode('utf-8').strip().split(',')):
                if not value:
                    continue
                if notes_stack.empty():
                    notes_stack.push([index, value])
                    continue
                top = notes_stack.peek()
                root = []
                while not notes_stack.empty() and top[0] >= index:

                    note_item = notes_stack.pop()
                    while not root_stack.empty() \
                          and root_stack.peek()[0] == note_item[0]:
                        if note_item[0] == 1:
                            root = [{note_item[1]: root}]
                            root_stack.push([1, root[0]])
                        else:
                            root = [root_stack.pop()[1][0], {note_item[1]: root}]

                        note_item = notes_stack.pop()
                        top = note_item

                    root = [{note_item[1]: root}]
                    if notes_stack.empty():
                        notes_stack.push(top)
                    if top[0] == index:
                        if index == 1:
                            root_stack.push([index, root[0]])
                        else:
                            root_stack.push([index, root])
                    top = notes_stack.peek()
                notes_stack.push([index, value])

        while not root_stack.empty():
            root.append(root_stack.pop()[1])
        return {notes_stack.pop()[1]: root[::-1]}


print(csv2json('./concepts.txt'))
