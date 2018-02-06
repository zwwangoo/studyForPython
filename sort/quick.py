import unittest


def quick_sort(data):
    """
    快速排序是对冒泡排序的一种改进。
    通过一趟排序将要排序的数据分割独立的两部分，
    一部分所有数据都比另一部分的所有数据都要小，
    然后再按照此方法对这两个部分分别进行快速排序，
    整个过程可以递归进行，以达到整个数据变成有序序列。
    :param data:
    :return:
    """
    if len(data) <= 1:
        return data
    pivot = data[0]  # 从数列中挑出一个元素作为基准数。

    # 将比基准数大的放到右边，小于或等于它的数都放到左边。
    left = quick_sort([x for x in data[1:] if x >= pivot])
    right = quick_sort([x for x in data[1:] if x < pivot])

    return right + [pivot] + left


class QuickSort(unittest.TestCase):
    def setUp(self):
        self.data = [1, 12, 78, 5, 8, 11, 2]
        self.result = [1, 2, 5, 8, 11, 12, 78]

    def test_sort(self):
        self.assertEqual(self.result, quick_sort(self.result))


if __name__ == "__main__":
    unittest.main()