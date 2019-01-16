# coding: utf-8
from ..my_base.my_stack import Stack
from ..my_base.my_node import Node
# ----------------------------------------------------------------
# ----------------------------------------------------------------


def remove_last_node(head, k):
    """
    2018-12-21
    在单链表中删除倒数第k个节点
    ---
    如果链表长度为N，时间复杂度也达到O(N)，额外空间复杂度达到O(1)
    """
    if not head or k < 1:
        return head
    tag_head = head
    while tag_head:
        k -= 1
        tag_head = tag_head.next
    if k == 0:
        return head.next
    if k < 0:
        tag_head = head
        while k != -1:
            k += 1
            tag_head = tag_head.next
        tag_head.next = tag_head.next.next
    return head


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def remove_mid_node(head):
    """
    2018-12-24
    删除链表中间的元素
    """
    if not head or not head.next:
        return head
    if not head.next.next:
        return head.next

    pre = head
    cur = head.next.next
    while cur.next and cur.next.next:
        pre = pre.next
        cur = cur.next.next

    pre.next = pre.next.next
    return head


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def remove_by_ratio(head, a, b):
    """
    2018-12-24
    删除链表 a/b处的元素
    """
    import math
    if a < 1 or a > b:
        return head
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next

    n = math.ceil(n * a / b)
    if n == 1:
        return head.next
    if n > 1:
        cur = head
        while n != 2:
            n -= 1
            cur = cur.next
        cur.next = cur.next.next
    return head


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def reverse_node(head):
    """
    2018-12-25
    翻转链表
    """
    pre = None
    next = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def reverse_part_node(head, from1, to):
    """
    2018-12-26
    翻转部分单向链表
    ---
    给定一个单向链表的头节点head，以及两个整数from和to，
    在单向链表上把第from个节点到第to个节点这一部分进行翻转。

    """
    length = 0
    node1 = head
    fpre = None
    tpos = None
    while node1:
        length += 1
        fpre = node1 if length == from1 - 1 else fpre
        tpos = node1 if length == to + 1 else tpos
        node1 = node1.next
    if from1 > to or from1 < 1 or to > length:
        return head
    node1 = fpre.next if fpre else head
    node2 = node1.next
    node1.next = tpos
    next = None
    while node2 != tpos:
        next = node2.next
        node2.next = node1
        node1 = node2
        node2 = next
    if fpre:
        fpre.next = node1
        return head
    return node1


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def jpsephus_kill_node(head, m):
    """
    2018-12-27
    环形单链表的约瑟夫问题
    ---
    据说著名犹太历史学家Josephus有过以下故事：
    在罗马人占领乔塔伯特后，39个犹太人与Josephus以及他的朋
    友躲到一个洞里，39个犹太人决定宁愿死也不要被敌人抓住，
    于是决定了一个自杀方式，41个人排成一个圆圈，由第1个人开
    始报数，报到3的人就自杀，然后再由下一个人重新报1，报数
    到3的人再自杀，以此下去，知道最后剩下一个人时，那个人可
    以自由选择自己的命运。这就是著名的约瑟夫问题。
    现请用单向环形链表描述该结构并呈现整个自杀过程。
    """
    if not head or head.next == head or m < 1:
        return head

    last = head
    while last.next != head:
        last = last.next

    count = 0
    while head != last:
        count += 1
        if count == m:
            last.next = head.next
            count = 0
        else:
            last = last.next
        head = last.next
    return head


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def is_palindroome_node(head):
    '''
    2018-12-28
    判断一个链表是否为回文
    ---
    给定一个链表的头节点head，判断该链表是否为回文结构。
    如果链表长度为N，时间复杂度也达到O(N)，额外空间复杂度达到O(1)
    '''
    if not head or not head.next:
        return head

    n1 = head
    n2 = head
    # 查找中间节点
    # n2跨两步，n1跨一步，当n2遍历结束的时候，n1指向的就是中间节点
    while n2.next and n2.next.next:
        n1 = n1.next
        n2 = n2.next.next

    n2 = n1.next  # 右部分第一个节点
    n1.next = None  # mid.next ->None
    n3 = None
    while n2:  # 右半边反转
        n3 = n2.next
        n2.next = n1
        n1 = n2
        n2 = n3

    n3 = n1.next  # 保存最后一个节点
    n2 = head  # 左边第一个节点
    res = True

    while n1 and n2:
        if n1.value == n2.value:
            n1 = n1.next
            n2 = n2.next
        else:
            res = False
            break

    # 还原链表
    n1 = n3.next
    n3.next = None

    while n1:
        n2 = n1.next
        n1.next = n3
        n3 = n1
        n1 = n2
    return res


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def merge_two_nodes(head1, head2):
    """
    2019-01-13
    合并两个有序的单链表
    ---
    给定两个有序单链表的头节点head1和head2，请合并两个有序连表，合并
    后依然有序，并返回合并后链表的头节点。
    """
    if not head1 or not head2:
        return head1 if head1 else head2

    head = head1 if head1.value < head2.value else head2
    cur1 = head1 if head1 == head else head2
    cur2 = head2 if head1 == head else head1
    pre = None
    while cur1 and cur2:
        if cur1.value <= cur2.value:
            pre = cur1
            cur1 = cur1.next
        else:
            next = cur2.next
            pre.next = cur2
            cur2.next = cur1
            pre = cur2
            cur2 = next
    pre.next = cur1 if cur1 else cur2
    return head


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def list_partition(head, pivot):
    """
    2019-01-14
    将单链表按某值划分成左边小、中间相等、右边大的形式。
    ---
    给定一个单向链表的头节点head，节点的值类型是整形，在给定一个整数pivot。
    实现一个调整链表的函数，将链表调整为左边部分都是值小于pivot的节点，中间
    部分都是值等于pivot的节点，右部分都是值大于pivot的节点。
    ---
    思路：
    将原链表中的所有节点依次分进三个链表，三个链表分别代表左部分、中间部分、
    右部分。
    """
    s_head = s_last = e_head = e_last = b_head = b_last = None
    while head:
        next = head.next
        head.next = None
        if head.value < pivot:
            if s_head is None:
                s_head = head
            else:
                s_last.next = head
            s_last = head
        elif head.value == pivot:
            if e_head is None:
                e_head = head
            else:
                e_last.next = head
            e_last = head
        else:
            if b_head is None:
                b_head = head
            else:
                b_last.next = head
            b_last = head
        head = next

    if s_last:
        s_last.next = e_head
        e_last = e_last if e_last else s_last

    if e_last:
        e_last.next = b_head
    return s_head or e_head or b_head


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def add_lists(head1, head2):
    """
    2019-01-14
    两个单链表生成相加链表
    ---
    假设链表中每一个节点的值都在0-9之间，那么链表整体就可以代表一个整数。
    给定两个这种链表的头节点head1和head2，生成两个整数相加值的结果链表。
    """
    stack1 = Stack()
    stack2 = Stack()

    while head1:
        stack1.push(head1.value)
        head1 = head1.next

    while head2:
        stack2.push(head2.value)
        head2 = head2.next

    ca = 0  # 表示是否进位
    head = None
    while not (stack1.empty() and stack1.empty()):
        s1 = 0 if stack1.empty() else stack1.pop()
        s2 = 0 if stack2.empty() else stack2.pop()

        n = s1 + s2 + ca
        node = Node(n % 10)
        node.next = head
        head = node
        ca = n // 10

    if ca == 1:  # 最高位进位处理
        node = Node(1)
        node.next = head
        head = node

    return head


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def relocate(head):
    """
    2019-01-15
    按照左右半区的方式重新组合单链表
    ---
    给定一个单链表的头节点head，链表长度为N，如果N为偶数，那么前N/2个节
    点算左半区，后N/2算右半区，如果N为奇数，那么前N/2各节点算左半区，后
    N/2+1个节点算右半区。左半区到右半区依次记为L1->L2->...，右半区记为
    R1->R2->...，请将单链表调整成L1->R1->L2->R2->L3->...
    """
    if not head or not head.next:
        return
    left = head
    mid = head
    right = head.next
    while right.next and right.next.next:
        mid = mid.next
        right = right.next.next
    right = mid.next
    mid.next = None

    while left.next:
        next = right.next
        right.next = left.next
        left.next = right
        left = right.next
        right = next
    left.next = right


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def remove_value(head, num):
    """
    2019-01-16
    在单链表中，删除指定值的节点
    ---
    给定一个链表的头节点head和一个整数num，实现函数将值为num的节点全部删除。
    """

    while head:
        if head.value == num:
            head = head.next
        else:
            break

    pre = cur = head
    while cur:
        if cur.value == num:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return head


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def remove_rep1(head):
    """
    2019-01-16
    删除无序单链表中值重复出现的节点
    ---
    给定一个无序单链表的头节点head，删除其中值重复出现的节点。
    要求：如果链表长度为N，时间复杂度达到O(N)
    """
    if not head:
        return None
    pre = head
    cur = head.next
    d = {head.value: 1}
    while cur:
        if d.get(cur.value):
            pre.next = cur.next
        else:
            d.update({cur.value: 1})
            pre = cur
        cur = cur.next
    return head


def remove_rep2(head):
    """
    2019-01-16
    删除无序单链表中值重复出现的节点
    ---
    给定一个无序单链表的头节点head，删除其中值重复出现的节点。
    要求：额外空间复杂度为O(1)
    """
    if not head:
        return None

    pre = None
    next = None
    cur = head
    while cur:
        pre = cur
        next = cur.next
        while next:
            if next.value == cur.value:
                pre.next = next.next
            else:
                pre = next
            next = next.next
        cur = cur.next
    return head
