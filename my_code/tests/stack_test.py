import pytest
from ..codes.about_stack import (
    MyStack, TwoStacksQueue, reverse_stack,
    hanoi_problem1, hanoi_problem2, get_max_window,
    get_max_window1,
)
from ..my_base.my_stack import create_stack


def test_my_stack_get_min():
    stack1 = MyStack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    assert stack1.get_min() == 1
    stack1.push(0)
    assert stack1.get_min() == 0
    assert stack1.pop() == 0
    assert stack1.pop() == 3
    assert stack1.pop() == 2
    assert stack1.pop() == 1
    stack1.push(5)
    assert stack1.pop() == 5
    stack1.push(4)
    assert stack1.pop() == 4


def test_two_stacks_queue():
    tsq = TwoStacksQueue()
    tsq.add(1)
    tsq.add(2)

    assert tsq.poll() == 1
    assert tsq.peek() == 2
    assert tsq.add(3) is None
    assert tsq.poll() == 2
    assert tsq.poll() == 3

    with pytest.raises(RuntimeError):
        tsq.poll()


def test_reverse_stack():
    stack1 = create_stack([1, 2, 3, 4, 5])
    reverse_stack(stack1)
    assert stack1.pop() == 1
    assert stack1.pop() == 2
    assert stack1.pop() == 3
    assert stack1.pop() == 4
    assert stack1.pop() == 5
    assert stack1.empty()


def test_hanoi_problem():
    assert hanoi_problem1(2) == hanoi_problem2(2)
    assert hanoi_problem1(3) == hanoi_problem2(3)
    assert hanoi_problem1(4) == hanoi_problem2(4)


def test_get_max_window():
    assert get_max_window([4, 3, 5, 4, 3, 3, 6, 7], 3) == [
        5, 5, 5, 4, 6, 7,
    ]
    assert get_max_window([3, 6, 7], 3) == [7]
    assert get_max_window1([4, 3, 5, 4, 3, 3, 6, 7], 3) == [
        5, 5, 5, 4, 6, 7,
    ]
    assert get_max_window1([3, 6, 7], 3) == [7]
