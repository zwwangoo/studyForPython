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
