import sys
import enum
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
    """
    2019-01-08
    两个栈组成的队列。
    ---
    编写一个类，用两个栈实现队列，支持队列的基本操作(add, poll, peek)
    """
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


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def get_and_remove_last_element(stack):
    result = stack.pop()
    if stack.empty():
        return result
    else:
        last = get_and_remove_last_element(stack)
        stack.push(result)
        return last


def reverse_stack(stack):
    """
    2019-01-10
    仅使用递归函数和栈操作逆序一个栈
    ---
    只能使用递归函数实现，不能使用其他数据结构
    """
    if stack.empty():
        return
    else:
        last = get_and_remove_last_element(stack)
        reverse_stack(stack)
        stack.push(last)


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def sort_stack_by_stack(stack):
    """
    2019-01-10
    用一个栈实现另外一个栈的排序
    ---
    一个栈中元素的类型为整数，现在想将该栈从栈顶到底按大到小的顺序排序，
    只许申请一个栈，除此之外，可以申请新的变量，但不能申请额外的数据结构。
    """
    help = Stack()
    while not stack.empty():
        cur = stack.pop()
        while not help.empty and help.peek() < cur:
            stack.push(help.pop())
        help.push(cur)

    while not help.empty:
        stack.push(help.pop())


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def hanoi_problem1(num, left='left', mid='mid', right='right'):
    """
    2019-01-10
    递归的方法解决汉诺塔问题
    ---
    修改部分游戏规则：
    限制不能从最左侧的塔直接移动到最右侧，反之也不行，而是必须经过中间，
    当塔有N层的时候，打印最优移动过程和最优移动总步数。
    ---
    思路分析：
    多层塔中，从最上到最下依次为1~N，则有如下判断

    “左”-->“中”(“右”-->“中”，“中”-->“左”， “中”-->“右” 步骤同理)
    1、如果剩下的N层塔都在“左”，希望全部移到“中”，则有三个步骤。
    1)将1~N-1层塔全部从“左”移到“右”，明显交个递归过程。
    2)将第N层塔从“左”移到“右”。
    3)再将1~N-1层塔全部从“右”移到中，明显也交个递归过程。

    “左”-->“右”(“右”-->“左” 步骤同理)
    2、如果剩下的N层塔都在左，希望全部移到“右”，则有五个步骤。
    1)将1~N-1层塔先全部从“左”移到“右”，明显交给递归过程。
    2)将第N层塔从“左”移到“中”。
    3)将1~N-1层塔全部从“右”移到“左”，明显交给递归过程。
    4)将第N层塔从“中”移到“右”。
    5)最后将1~N-1层塔全部从“左”移到“右”，明显交给递归过程。

    """
    if num < 1:
        return 0
    else:
        return propess(num, left, mid, right, right, left)


def propess(num, left, mid, right, from_s, to_s):
    if num == 1:
        if from_s == mid or to_s == mid:
            print('Move 1 from {} to {}'.format(from_s, to_s))
            return 1
        else:
            print('Move 1 from {} to {}'.format(from_s, mid))
            print('Move 1 from {} to {}'.format(mid, to_s))
            return 2
    if from_s == mid or to_s == mid:  # “左”-->“中”
        another = right if from_s == left or to_s == left else left
        part1 = propess(num - 1, left, mid, right, from_s, another)
        part2 = 1
        print('Move {} from {} to {}'.format(str(num), from_s, to_s))
        part3 = propess(num - 1, left, mid, right, another, to_s)
        return part1 + part2 + part3
    else:  # "左”-->“右"
        part1 = propess(num - 1, left, mid, right, from_s, to_s)
        part2 = 1
        print('Move {} from {} to {}'.format(str(num), from_s, mid))
        part3 = propess(num - 1, left, mid, right, to_s, from_s)
        part4 = 1
        print('Move {} from {} to {}'.format(str(num), mid, to_s))
        part5 = propess(num - 1, left, mid, right, from_s, to_s)
        return part1 + part2 + part3 + part4 + part5


# ----------------------------------------------------------------
# ----------------------------------------------------------------


class Action(enum.Enum):
    No = 0
    LToM = 1
    MToL = 2
    MToR = 3
    RToM = 4


def hanoi_problem2(num, left='left', mid='mid', right='right'):
    """
    2019-01-11
    非递归的方法解决汉诺塔问题——用栈来模拟过程
    ---
    修改部分游戏规则：
    限制不能从最左侧的塔直接移动到最右侧，反之也不行，而是必须经过中间，
    当塔有N层的时候，打印最优移动过程和最优移动总步数。
    ---
    """
    ls = Stack()
    ms = Stack()
    rs = Stack()
    for stack in (ls, ms, rs):
        stack.push(sys.maxsize)

    for i in range(num, 0, -1):
        ls.push(i)

    record = [Action.No]
    step = 0

    while rs.size() != num + 1:
        step += f_stack_to_stack(
            record, Action.MToL, Action.LToM, ls, ms,
            left, mid,
        )
        step += f_stack_to_stack(
            record, Action.LToM, Action.MToL, ms, ls,
            mid, left,
        )
        step += f_stack_to_stack(
            record, Action.RToM, Action.MToR, ms, rs,
            mid, right,
        )
        step += f_stack_to_stack(
            record, Action.MToR, Action.RToM, rs, ms,
            right, mid,
        )
    return step


def f_stack_to_stack(record, pre_no_act, now_act, fstack, tstack, froms, tos):
    if pre_no_act != record[0] and fstack.peek() < tstack.peek():
        # 注意的是：相反的动作不会发生。
        tstack.push(fstack.pop())
        print('Move {} from {} to {}'.format(str(tstack.peek()), froms, tos))
        record[0] = now_act
        return 1
    else:
        return 0


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def get_max_window(array, w):
    """
    2019-01-11
    生成窗口最大值数组
    ---
    有一个整形数组array和一个大小为w的窗口从数组的最左边滑到最右边，
    窗口每次向右边划一个位置，如果数组长度为n，窗口大小为w，则一共
    产生n-w+1个窗口的最大值。
    """
    if len(array) == 0 or w < 1 or len(array) < w:
        return None
    q_max = []  # 用来存放array中的下标
    i = 0
    res = []
    for i in range(len(array)):
        while len(q_max) != 0 and array[i] >= array[q_max[-1]]:
            # 弹出array[i] <= array[j] 的q_max中的j下标
            q_max.remove(q_max[-1])

        q_max.append(i)

        if q_max[0] == i - w:
            q_max.remove(q_max[0])

        if i >= w - 1:
            res.append(array[q_max[0]])
    return res


def get_max_window1(array, w):
    """
    2019-01-11
    生成窗口最大值数组
    ---
    用了python的内置函数max
    """
    if len(array) == 0 or w < 1 or len(array) < w:
        return None
    res = []
    for i in range(len(array)):
        if i + w == len(array) + 1:
            break
        res.append(max(array[i:i + w]))
    return res
