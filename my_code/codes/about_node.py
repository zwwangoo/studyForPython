# coding: utf-8
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
    给定一个单向链表的头结点head，以及两个整数from和to，
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
    给定一个链表的头结点head，判断该链表是否为回文结构。
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


def merge_two_nodes(head1, head2):
    """
    2019-01-13
    合并两个有序的单链表
    ---
    给定两个有序单链表的头结点head1和head2，请合并两个有序连表，合并
    后依然有序，并返回合并后链表的头结点。
    """
    if not head1 or not head2:
        return head1 if head1 else head2

    head = head1 if head1.value <= head2.value else head2
    cur1 = head1 if head == head1 else head2
    cur2 = head2 if head == head1 else head1
    pre = None
    while cur1 and cur2:
        if cur1.value < cur2.value:
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
