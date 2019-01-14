class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_nodes(column):
    column = list(column)[::-1]
    head = None
    for i in column:
        node = Node(i)
        node.next = head
        head = node
    return head


def read_nodes(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values
