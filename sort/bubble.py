import unittest

__string = """
冒泡排序的python实现方式。
"""


def bubble_soft_1(data):
    """冒泡排序（升序）
    这个排序的过程是先排小数
    :param data: 待排序的数组
    :return: 排完序的数组
    """
    length = len(data)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if data[i] > data[j]:
                data[j], data[i] = data[i], data[j]
    return data


def bubble_soft_2(data):
    """冒泡排序（升序）
    这个排序的过程是先排大数
    :param data: 待排序的数组
    :return: 排完序的数组
    """
    length = len(data)
    for i in range(length - 1):
        for j in range(length - 1):
            if data[j + 1] < data[j]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def bubble_soft_3(data):
    """冒泡排序（升序）优化
    这个排序的过程是先排大数，
    设置了一个标志，某一趟排序时并没有进行数据交换，则说明所有数据已经有序
    这样做是优化了当数组有序的时候，进行的不必要遍历
    :param data: 待排序的数组
    :return: 排完序的数组
    """
    length = len(data)
    for i in range(length - 1):
        change = False
        for j in range(length - 1):
            if data[j + 1] < data[j]:
                data[j], data[j + 1] = data[j + 1], data[j]
                change = True
        if not change:
            break
    return data


class BubbleSortTest(unittest.TestCase):
    def setUp(self):
        self.data_a = [1, 12, 78, 5, 8, 11, 2]
        self.data_b = [1, 12, 78, 5, 8, 11, 2]
        self.data_c = [1, 12, 78, 5, 8, 11, 2]
        self.result = [1, 2, 5, 8, 11, 12, 78]

    def test_sort_1(self):
        self.assertEqual(self.result, bubble_soft_1(self.data_a))

    def test_sort_2(self):
        self.assertEqual(self.result, bubble_soft_2(self.data_b))

    def test_sort_3(self):
        self.assertEqual(self.result, bubble_soft_3(self.data_c))


if __name__ == "__main__":
    unittest.main()
