from ..my_base.my_node import create_nodes, read_nodes
from ..codes.about_node import (
    remove_mid_node, remove_last_node, remove_by_ratio, reverse_node,
    reverse_part_node, is_palindroome_node,
)


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
