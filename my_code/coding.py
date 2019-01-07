# coding: utf-8
# ----------------------------------------------------------------
# ----------------------------------------------------------------
from .my_base.my_stack import Stack


def is_deformation(string1, string2):
    """
    2018-11-13
    判断两个字符串是否为互为变形词
    ---
    给定两个字符串str1和str2，如果str1和str2中出现的字符种类一样且每种字符出现的
    次数也一样，那么str1和str2互为变形词
    """
    if not string1 or not string2 or len(string1) != len(string2):
        return False

    count_dict = {}
    for char in string1:
        count = count_dict.get(char)
        if count is not None:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    for char in string2:
        has_char = count_dict.get(char, 0)
        if has_char == 0:
            return False
        else:
            count_dict[char] -= 1
    return True

# ----------------------------------------------------------------
# ----------------------------------------------------------------


def num_sum(string1):
    """
    2018-11-14
    字符串中，数字子串的求和
    ---
    给定一个字符串，求其中全部数字串所代表的数字之和, 忽略小数点
    数字左侧的-符号表示数字的正负，负负得正
    """
    if not string1:
        return 0
    num = res = 0
    posi = True
    for i in range(len(string1)):
        cur = string1[i]
        if '0' <= cur <= '9':
            cur = int(cur)
            num = num * 10 + (cur if posi else -cur)
        else:
            res += num
            num = 0
            if cur == '-':
                if i > 0 and string1[i - 1] == '-':
                    posi = not posi
                else:
                    posi = False
            else:
                posi = True
    res += num
    return num

# ----------------------------------------------------------------
# ----------------------------------------------------------------


def remove_k_zeros(string1, k):
    """
    2018-11-15
    去掉字符串中连续出现的k个0的子串
    ---
    给定一个字符串string1和一个整数k， 如果string1中正好有连续的k个‘0’字符出现时，
    把k个连续的'0'字符去除，返回处理后的字符串
    """
    count = 0
    str1 = ''
    for char in string1:
        if char == '0':
            count += 1
        else:
            if count != k:
                str1 = str1 + '0' * count
            str1 += char
            count = 0

    if count != 0 and count != k:
        str1 = str1 + '0' * count

    return str1

# ----------------------------------------------------------------
# ----------------------------------------------------------------


def is_rotation(a, b):
    """
    2018-11-17
    判断两个字符串是否互为旋转词
    ---
    如果一个字符串str，把字符串str前面任意的部分挪到后面形成的字符串叫做str的旋转词。
    比如str=‘12345’，str的旋转词有‘12345’、'23451'、'34512'、'45123'、'51234'
    """
    if not a or not b or len(a) != len(b):
        return False
    r = b * 2
    return a in r

# ----------------------------------------------------------------
# ----------------------------------------------------------------


def convert(string):
    """
    2018-11-17
    将整数字符串转成整数值
    ---
    给定一个字符串str，如果str符号日常书写的整数形式，并且属于32位整数的范围，
    返回str所代表的整数值，否则返回0
    """
    if not string or not string.split():
        return 0
    if not is_valid(string):
        return 0

    minq = -214748364
    minr = -8
    posi = False if string[0] == '-' else True
    res = 0
    for char in string[0 if posi else 1:]:
        cur = 0 - int(char)
        if res < minq or (res == minq and cur < minr):
            return 0
        res = res * 10 + cur
    if res == -2147483648 and posi:
        return 0
    return res if not posi else -res


def is_valid(string):
    if string[0] != '-' and not '0' <= string[0] <= '9':
        return False
    if string[0] == '-' and (len(string) == 1 or string[1] == '0'):
        return False
    if string[0] == '0' and len(string) > 1:
        return False
    for i in string[1:]:
        if not '0' <= i <= '9':
            return False
    return True

# ----------------------------------------------------------------
# ----------------------------------------------------------------


def replace(str1, from1, to1):
    """
    2018-11-19
    替换字符串中连续出现的指定字符串
    ---
    给定三个字符串str1、from1和to1，已知from1字符串中无重复字符，
    把str中所有from1的子串全部替换成to1字符串，对连续出现from1的
    部分要求只替换一个to字符串，返回最终的结果字符串。
    """
    str2 = ''
    match = 0
    for index, value in enumerate(str1):
        if value == from1[match]:
            match += 1
            if match == len(from1):
                str2 += '0' * match
                match = 0
        else:
            if match != 0:
                str2 += str1[index - match:index]
            str2 += value
            match = 0

    res = ''
    for index, value in enumerate(str2):
        if value != '0':
            res += value
        else:
            if index == 0 or str2[index - 1] != '0':
                res += to1
    return res

# ----------------------------------------------------------------
# ----------------------------------------------------------------


def get_count_string(str1):
    """
    2018-11-20
    字符串的统计字符串
    ---
    给定一个字符串str1，返回str1的统计字符串。例如"aaabbaddffc"的
    统计字符串为"a_3_b_2_a_1_d_2_f_2_c_1"
    """

    if not str1 or not str1.strip():
        return ''

    res = ''
    num = 1
    for index in range(1, len(str1)):
        if str1[index] == str1[index - 1]:
            num += 1
        else:
            res += str1[index - 1] + '_' + str(num) + '_'
            num = 1

    res += str1[-1] + '_' + str(num)
    return res

# ----------------------------------------------------------------
# ----------------------------------------------------------------


def is_uniquel(chars):
    """
    2018-11-21
    判断字符数组中是否所有的字符都只出现过一次
    ---
    给定一个字符类型chars[]，判断chars中是否所有的字符都只出现过
    一次，请根据以下不同的两种要求实现两个函数
    1. 实现时间复杂度为O(N)的方法
    2. 在保证额外空间复杂度为O(1)的前提下，请实现时间复杂度尽量低
    的方法(暂未实现)
    """
    if len(chars) == 0:
        return False
    count = {}
    for chars in chars:
        if count.get(chars):
            return False
        else:
            count[chars] = 1
    return True

# ----------------------------------------------------------------
# ----------------------------------------------------------------


def get_index(strs, str1):
    """
    2018-11-22
    在有序但含有空的数组中查找字符串
    ---
    给定一个字符串数组strs，在strs中有些位置位''，但不为''的位置
    上，其字符串是按照字典顺序由小到大依次出现的。 再给定一个字
    符串str，请返回str在strs中出现的最左的位置。
    本地的解法尽可能使用了二分查找。
    """
    if not strs or not str1:
        return -1
    res = -1
    left = 0
    right = len(strs) - 1

    while left < right:
        mid = (left + right) // 2
        if not strs[mid] and strs[mid] == str1:
            right = mid - 1
            res = mid
        elif not strs[mid]:
            if strs[mid] > str1:
                left = mid + 1
            else:
                right = mid - 1
        else:
            i = mid - 1
            while not strs[i] and i >= left:
                i -= 1
            if i < left or strs[i] < strs[left]:
                left = mid + 1
            else:
                res = i if strs[i] == str1 else res
                right = i - 1
    return res


def rotate_word(chas):
    """
    2018-11-28
    翻转字符串
    ---
    给定一个字符类型的数组chas，请在单词间做逆序调整。
    只要做到单词顺序逆序即可，对空格的位置没有特殊要求
    """
    j = len(chas)
    i = j - 1
    res = ''
    while i > 0:
        if chas[i] == ' ':
            res += chas[i + 1:j] + ' '
            j = i
        i -= 1
    if i == 0:
        res += chas[i:j]
    return res


def min_distance(strs, str1, str2):
    """
    2018-11-30
    数组中两个字符串的最小距离
    ---
    给定一个字符串数组strs，再给定两个字符串str1和str2，
    返回strs中str1和str2的最小距离，如果str1或str2为null，
    或不在strs中，返回-1
    """
    import sys
    if not(str1 and str2):
        return -1
    if str1 == str2:
        return 0

    last1 = last2 = -1
    mind = sys.maxsize

    i = 0
    while i < len(strs):
        if strs[i] == str1:
            mind = mind if last2 == -1 else i - last2
            last1 = i
        elif strs[i] == str2:
            mind = mind if last1 == -1 else i - last1
            last2 = i
        i += 1
    return -1 if mind == sys.maxsize else mind


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
