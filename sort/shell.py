# coding: utf-8


def shell_sort(data):
    """
    希尔(Shell)排序: 缩小增量排序，它是一种插入排序。
    它是直接插入排序算法的一种威力加强版
    :param data:
    :return:
    """
    length = len(data)
    step = length // 2  # 初始步长
    while step > 0:
        # 其实下面执行的就是插入排序啦，只不过需要注意步长
        for i in range(step, length):  # 每一列进行插入排序 , 从step 到 n-1
            now_num = data[i]
            j = i
            while j >= step and data[j - step] > now_num:  # 插入排序
                data[j] = data[j - step]
                j -= step
            data[j] = now_num
        step //= 2  # 重新设置步长
    return data
