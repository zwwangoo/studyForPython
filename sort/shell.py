import unittest


def shell_sort(data):
    """
    希尔(Shell)排序: 缩小增量排序，它是一种插入排序。
    它是直接插入排序算法的一种威力加强版
    :param data:
    :return:
    """
    n = len(data)
    step = n // 2  # 初始步长
    while step > 0:
        # 其实下面执行的就是插入排序啦，只不过需要注意步长
        for i in range(step, n):  # 每一列进行插入排序 , 从step 到 n-1
            now_num = data[i]
            j = i
            while j >= step and data[j - step] > now_num:  # 插入排序
                data[j] = data[j - step]
                j = j - step
            data[j] = now_num
        step = step // 2  # 重新设置步长
    return data


class ShellSortTest(unittest.TestCase):
    def setUp(self):
        self.data = [1, 12, 78, 5, 8, 11, 2]
        self.result = [1, 2, 5, 8, 11, 12, 78]

    def test_sort(self):
        self.assertEqual(self.result, shell_sort(self.data))


if __name__ == "__main__":
    unittest.main()
