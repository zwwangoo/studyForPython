from ..my_base.my_node import create_nodes, read_nodes
from ..codes.about_node import (
    remove_mid_node, remove_last_node, remove_by_ratio, reverse_node,
    reverse_part_node, is_palindroome_node, list_partition, add_lists,
    relocate, merge_two_nodes,
)


def test_remove_last_node():

    assert read_nodes(remove_last_node(create_nodes(range(5)), 3)) == [
        0, 1, 3, 4,
    ]
    assert read_nodes(remove_last_node(create_nodes(range(10)), 11)) == [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    ]
    assert read_nodes(remove_last_node(create_nodes(range(10)), 0)) == [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    ]


def test_remove_mid_node():
    assert read_nodes(remove_mid_node(create_nodes(range(2)))) == [1]
    assert read_nodes(remove_mid_node(create_nodes(range(10)))) == [
        0, 1, 2, 3, 5, 6, 7, 8, 9,
    ]
    assert read_nodes(remove_mid_node(create_nodes(range(5)))) == [
        0, 1, 3, 4,
    ]


def test_remove_by_ratio():
    assert read_nodes(remove_by_ratio(create_nodes(range(2)), 1, 2)) == [1]
    assert read_nodes(remove_by_ratio(create_nodes(range(7)), 5, 7)) == [
        0, 1, 2, 3, 5, 6,
    ]
    assert read_nodes(remove_by_ratio(create_nodes(range(7)), 5, 6)) == [
        0, 1, 2, 3, 4, 6,
    ]
    assert read_nodes(remove_by_ratio(create_nodes(range(7)), 1, 6)) == [
        0, 2, 3, 4, 5, 6,
    ]


def test_reverse_node():
    assert read_nodes(reverse_node(create_nodes(range(5)))) == [4, 3, 2, 1, 0]
    assert read_nodes(reverse_node(create_nodes(range(1)))) == [0]


def test_reverse_part_node():
    assert read_nodes(reverse_part_node(create_nodes(range(5)), 2, 4)) == [
        0, 3, 2, 1, 4,
    ]
    assert read_nodes(reverse_part_node(create_nodes(range(5)), 0, 4)) == [
        0, 1, 2, 3, 4,
    ]
    assert read_nodes(reverse_part_node(create_nodes(range(4)), 1, 4)) == [
        3, 2, 1, 0,
    ]


def test_is_palindroome_node():
    assert is_palindroome_node(create_nodes([1, 2, 3, 3, 2, 1]))
    assert not is_palindroome_node(create_nodes([1, 2, 3, 3]))


def test_merge_two_nodes():
    head1 = create_nodes([0, 2, 3, 7])
    head2 = create_nodes([1, 3, 5, 7, 9])
    assert read_nodes(merge_two_nodes(head1, head2)) == [
        0, 1, 2, 3, 3, 5, 7, 7, 9,
    ]


def test_list_partition():
    assert read_nodes(list_partition(create_nodes([9, 0, 4, 5, 1]), 3)) == [
        0, 1, 9, 4, 5,
    ]
    assert read_nodes(list_partition(create_nodes([7, 9, 1, 8, 5, 2]), 5)) == [
        1, 2, 5, 7, 9, 8,
    ]


def test_add_lists():
    assert read_nodes(
        add_lists(create_nodes([9, 3, 7]), create_nodes([6, 3])),
    ) == [
            1, 0, 0, 0,
    ]
    assert read_nodes(
        add_lists(create_nodes([8, 3, 7]), create_nodes([6, 3])),
    ) == [
            9, 0, 0,
    ]


def test_relocate():
    head = create_nodes([1, 2])
    relocate(head)
    assert read_nodes(head) == [1, 2]

    head = create_nodes([1, 2, 3, 4, 5])
    relocate(head)
    assert read_nodes(head) == [1, 3, 2, 4, 5]
