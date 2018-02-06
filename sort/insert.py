import unittest


def insert_sort(data):
    """
    插入排序（升序）
    :param data:
    :return:
    """
    length = len(data)
    for i in range(length):
        now = data[i]
        j = i - 1
        while j >= 0 and data[j] > now:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = now
    return data


class InsertSortTest(unittest.TestCase):
    def setUp(self):
        self.data = [1, 12, 78, 5, 8, 11, 2]
        self.result = [1, 2, 5, 8, 11, 12, 78]

    def test_insert(self):
        self.assertEqual(self.result, insert_sort(self.data))


if __name__ == "__main__":
    unittest.main()
