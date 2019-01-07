class Node(object):
    def __init__(self, value):
        self.value = value
        self.lChild = None
        self.rChild = None


def createBinaryTree():
    # 先序递归的方式创建二叉树，
    # 按先后次序输入二叉树中的节点，以#表示空树
    value = input('请输入当前节点的值（如果是空树，请用“#”表示）> ')
    if value == '#':
        root = None  # 当前节点为空
    else:
        root = Node(value)
        root.lChild = createBinaryTree()
        root.rChild = createBinaryTree()
    return root


if __name__ == '__main__':
    root = createBinaryTree()
    print('先序创建二叉树完毕！')
