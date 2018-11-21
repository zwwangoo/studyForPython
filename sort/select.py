# coding: utf-8


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
            data[index], data[i] = data[i], data[index]
    return data

