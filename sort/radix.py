# coding: utf-8


def RadixSort(input_list):
    """
    基数排序（升序）
    """

    def MaxBit(input_list):
        """
        求出数组中最大数的位数的函数
        """
        max_data = max(input_list)
        bits_num = 0
        while max_data:
            bits_num += 1
            max_data //= 10
        return bits_num

    def digit(num, d):
        """
        取数xxx上的第d位数字
        """
        p = 1
        while d > 0:
            d -= 1
            p *= 10
        return num // p % 10

    length = len(input_list)
    bucket = [0] * length

    for d in range(1, MaxBit(input_list) + 1):
        count = [0] * 10

        for i in range(0, length):
            count[digit(input_list[i], d)] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(0, length)[::-1]:
            k = digit(input_list[i], d)
            bucket[count[k] - 1] = input_list[i]
            count[k] -= 1
        for i in range(0, length):
            input_list[i] = bucket[i]

    return input_list
