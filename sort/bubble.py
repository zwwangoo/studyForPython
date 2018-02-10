
__string = """
冒泡排序的python实现方式。
"""


def bubble_sort_1(data):
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


def bubble_sort_2(data):
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


def bubble_sort_3(data):
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
