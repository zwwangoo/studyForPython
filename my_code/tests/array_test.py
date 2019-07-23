from ..codes.about_array import (
    spiral_order_print, rotate, print_matrix_zig_zag, two_sum,
)


def test_spiral_order_print():
    data1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    data2 = [
        [1, 2, 3, 4],
    ]
    data3 = [
        [1],
        [2],
        [3],
        [4],
    ]
    assert spiral_order_print(data1) == [
        1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10,
    ]
    assert spiral_order_print(data2) == [1, 2, 3, 4]
    assert spiral_order_print(data3) == [1, 2, 3, 4]


def test_rotate():
    data = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    assert rotate(data) == [
        [13, 9,  5,  1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]


def test_matrix_zig_zag():
    data = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    assert print_matrix_zig_zag(data) == [
        1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12,
    ]


def test_two_sum():
    nums = [2, 7, 11, 15]
    assert two_sum(nums, 9) == [0, 1]
