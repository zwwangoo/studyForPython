# coding: utf-8
# ----------------------------------------------------------------
# ----------------------------------------------------------------
from ..my_base.my_stack import Stack


def pre_order_recur(head):
    '''
    2019-03-11
    递归的方式实现二叉树的前序遍历
    '''
    if not head:
        return
    print(head.value)
    pre_order_recur(head.left)
    pre_order_recur(head.right)


def pre_order_un_recur(head):
    '''
    2019-03-11
    非递归的方式实现二叉树的前序遍历
    ---
    使用一个栈来保存信息。
    1 申请一个新的栈，记为stack，然后将头节点压入stack中，
    2 从stack中弹出栈顶节点，打印其值，再将其右孩子（不为空的话）先
    压stack中，最后将其左孩子（不为空的话）压入stack中，
    3 不断重复步骤2，直到stack为空，全部过程结束。
    '''
    if not head:
        return
    stack = Stack()
    stack.push(head)
    while not stack.empty():
        node = stack.pop()
        print(node.value)
        if node.right:
            stack.push(node.right)
        if node.left:
            stack.push(node.left)


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def in_order_recur(head):
    '''
    2019-03-11
    递归的方式实现二叉树的中序遍历
    '''
    if not head:
        return
    in_order_recur(head.left)
    print(head.value)
    in_order_recur(head.right)


def in_order_un_recur(head):
    '''
    2019-03-11
    非递归的方式实现二叉树的中序遍历
    ---
    使用一个栈来保存信息
    1 申请一个新的栈
    2 先将head压入栈中，对以head节点为头的整棵树来说，依把左边界压入栈中，即不停的令
    head=head.left。然后重复步骤2
    3 不断重复步骤2，直到发现head为空，此时从stack中弹出一个节点，记为node，打印node
    的值，并且让head=node.right,然后继续重复步骤2
    4 当stack为空且head为空时，整个过程停止。

    '''
    if not head:
        return
    stack = Stack()
    while not stack.empty() or head:
        if head:
            stack.push(head)
            head = head.left
        else:
            node = stack.pop()
            print(node.value)
            head = node.right


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def pos_order_recur(head):
    '''
    2019-03-11
    递归的方式实现二叉树的后序遍历
    '''
    if not head:
        return
    pos_order_recur(head.left)
    pos_order_recur(head.right)
    print(head.value)


def pos_order_unrecur(head):
    '''
    2019-03-11
    非递归的方式实现二叉树的后序遍历
    ---
    用两个栈实现后序遍历：
    1 申请一个栈s1，然后将头节点head压入s1中，
    2 从s1中弹出的节点记为node，然后依次将node的左孩子和又孩子压入s1中
    3 在整个过程中每一个从s1弹出的节点都放进s2中
    4 不断重复步骤2和3，直到s1为空，过程停止
    5 从s2中依次弹出节点并打印，打的顺序就是后序遍历的顺序。
    '''
    if not head:
        return
    s1 = Stack()
    s2 = Stack()
    s1.push(head)
    while not s1.empty():
        node = s1.pop()
        s2.push(node)
        if node.left:
            s1.push(node.left)
        if node.right:
            s1.push(node.right)
    while not s2.empty():
        print(s2.pop().value)
