import unittest


def select_sort(data):
    """
    选择排序
    :param data:
    :return:
    """
    length = len(data)
    for i in range(length):
        index = i
        for j in range(i+1, length):
            if data[j] < data[index]:
                index = j  # 记录当前循环中最小的数的索引
        if index != i:
            data[i] = data[index]
    return data


class SelectSortTest(unittest.TestCase):
    def setUp(self):
        self.data = [1, 12, 78, 5, 8, 11, 2]
        self.result = [1, 2, 5, 8, 11, 12, 78]

    def test_sort(self):
        self.assertEqual(self.result, select_sort(self.data))


if __name__ == "__main__":
    unittest.main()
