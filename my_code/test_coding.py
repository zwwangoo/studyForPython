from .coding import (
    convert, replace, get_count_string, is_uniquel,
    rotate_word, get_index, min_distance,
    remove_last_node, remove_mid_node, remove_by_ratio,
    reverse_node, reverse_part_node, is_palindroome_node,
)


class Node(object):
    def __init__(self, data):
        self.value = data
        self.next = None


def create_nodes(column):
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


def test_convert():
    assert convert('12346') == 12346
    assert convert('-12346') == -12346
    assert convert('-2147483648') == -2147483648
    assert convert('-2147483647') == -2147483647

    assert convert('-012346') == 0
    assert convert('-A') == 0
    assert convert('0') == 0
    assert convert('-') == 0
    assert convert('2147483648') == 0
    assert convert('-2147483649') == 0
    assert convert('4.3') == 0


def test_replace():
    assert replace('123abc', 'abc', '4567') == '1234567'
    assert replace('123', 'abc', '456') == '123'
    assert replace('123abcabc', 'abc', 'X') == '123X'

    assert replace('abcabc123', 'abc', 'X') == 'X123'


def test_get_count_string():
    assert get_count_string('aabbbcccf') == 'a_2_b_3_c_3_f_1'
    assert get_count_string('aaabcccff') == 'a_3_b_1_c_3_f_2'
    assert get_count_string('   ') == ''


def test_is_uniquel():
    assert is_uniquel(['a', 'b', 'c'])
    assert not is_uniquel(['1', '2', '1'])


def test_get_index():
    assert get_index(['', 'a', 'a', '', 'b'], 'a') == 1
    assert get_index(['', 'a', 'a', '', 'b'], 'c') == -1


def test_rotate_word():
    assert rotate_word('pig loves dog') == 'dog loves pig'
    assert rotate_word('I`m a student.') == 'student. a I`m'


def test_min_distance():
    assert min_distance(['CD'], 'CD', 'AB') == -1
    assert min_distance(['1', '3', '3', '3', '2', '3', '1'], '2', '1') == 2


def test_remove_last_node():

    assert read_nodes(remove_last_node(create_nodes(range(5)), 3)) == [
        4, 3, 1, 0,
    ]
    assert read_nodes(remove_last_node(create_nodes(range(10)), 11)) == [
        9, 8, 7, 6, 5, 4, 3, 2, 1, 0,
    ]
    assert read_nodes(remove_last_node(create_nodes(range(10)), 0)) == [
        9, 8, 7, 6, 5, 4, 3, 2, 1, 0,
    ]


def test_remove_mid_node():
    assert read_nodes(remove_mid_node(create_nodes(range(2)))) == [0]
    assert read_nodes(remove_mid_node(create_nodes(range(10)))) == [
        9, 8, 7, 6, 4, 3, 2, 1, 0,
    ]
    assert read_nodes(remove_mid_node(create_nodes(range(5)))) == [
        4, 3, 1, 0,
    ]


def test_remove_by_ratio():
    assert read_nodes(remove_by_ratio(create_nodes(range(2)), 1, 2)) == [0]
    assert read_nodes(remove_by_ratio(create_nodes(range(7)), 5, 7)) == [
        6, 5, 4, 3, 1, 0,
    ]
    assert read_nodes(remove_by_ratio(create_nodes(range(7)), 5, 6)) == [
        6, 5, 4, 3, 2, 0,
    ]
    assert read_nodes(remove_by_ratio(create_nodes(range(7)), 1, 6)) == [
        6, 4, 3, 2, 1, 0,
    ]


def test_reverse_node():
    assert read_nodes(reverse_node(create_nodes(range(5)))) == [0, 1, 2, 3, 4]
    assert read_nodes(reverse_node(create_nodes(range(1)))) == [0]


def test_reverse_part_node():
    assert read_nodes(reverse_part_node(create_nodes(range(5)), 2, 4)) == [
        4, 1, 2, 3, 0,
    ]
    assert read_nodes(reverse_part_node(create_nodes(range(5)), 0, 4)) == [
        4, 3, 2, 1, 0,
    ]
    assert read_nodes(reverse_part_node(create_nodes(range(4)), 1, 4)) == [
        0, 1, 2, 3,
    ]


def test_is_palindroome_node():
    assert is_palindroome_node(create_nodes([1, 2, 3, 3, 2, 1]))
    assert not is_palindroome_node(create_nodes([1, 2, 3, 3]))
