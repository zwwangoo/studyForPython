import pytest
from ..codes.about_stack import MyStack, TwoStacksQueue


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
