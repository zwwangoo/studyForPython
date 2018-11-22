# coding: utf-8
# ----------------------------------------------------------------
# ----------------------------------------------------------------

def is_deformation(string1, string2):
    """
    2018-11-13
    判断两个字符串是否为互为变形词
    ---
    给定两个字符串str1和str2，如果str1和str2中出现的字符种类一样且每种字符出现的
    次数也一样，那么str1和str2互为变形词
    """
    if not string1 or not string2 or len(string1) != len(string2):
        return False

    count_dict = {}
    for char in string1:
        count = count_dict.get(char)
        if count is not None:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    for char in string2:
        has_char = count_dict.get(char, 0)
        if has_char == 0:
            return False
        else:
            count_dict[char] -= 1
    return True

# ----------------------------------------------------------------
# ----------------------------------------------------------------

def num_sum(string1):
    """
    2018-11-14
    字符串中，数字子串的求和
    ---
    给定一个字符串，求其中全部数字串所代表的数字之和, 忽略小数点
    数字左侧的-符号表示数字的正负，负负得正
    """
    if not string1:
        return 0
    num = res = 0
    posi = True
    for i in range(len(string1)):
        cur = string1[i]
        if '0' <= cur <= '9':
            cur = int(cur)
            num = num * 10 + (cur if posi else -cur)
        else:
            res += num
            num = 0
            if cur == '-':
                if i > 0 and string1[i - 1] == '-':
                    posi = not posi
                else:
                    posi = False
            else:
                posi = True
    res += num
    return num

# ----------------------------------------------------------------
# ----------------------------------------------------------------

def remove_k_zeros(string1, k):
    """
    2018-11-15
    去掉字符串中连续出现的k个0的子串
    ---
    给定一个字符串string1和一个整数k， 如果string1中正好有连续的k个‘0’字符出现时，
    把k个连续的'0'字符去除，返回处理后的字符串
    """
    count = 0
    str1 = ''
    for char in string1:
        if char == '0':
            count += 1
        else:
            if count != k:
                str1 = str1 + '0' * count
            str1 += char
            count = 0

    if count != 0 and count != k:
        str1 = str1 + '0' * count

    return str1

# ----------------------------------------------------------------
# ----------------------------------------------------------------

def is_rotation(a, b):
    """
    2018-11-17
    判断两个字符串是否互为旋转词
    ---
    如果一个字符串str，把字符串str前面任意的部分挪到后面形成的字符串叫做str的旋转词。
    比如str=‘12345’，str的旋转词有‘12345’、'23451'、'34512'、'45123'、'51234'
    """
    if not a or not b or len(a) != len(b):
        return False
    r = b * 2
    return a in r

# ----------------------------------------------------------------
# ----------------------------------------------------------------

def convert(string):
    """
    2018-11-17
    将整数字符串转成整数值
    ---
    给定一个字符串str，如果str符号日常书写的整数形式，并且属于32位整数的范围，
    返回str所代表的整数值，否则返回0
    """
    if not string or not string.split():
        return 0
    if not is_valid(string):
        return 0

    minq = -214748364
    minr = -8
    posi = False if string[0] == '-' else True
    res = 0
    for char in string[0 if posi else 1:]:
        cur = 0 - int(char)
        if res < minq or (res == minq and cur < minr):
            return 0
        res = res * 10 + cur
    if res == -2147483648 and posi:
        return 0
    return res if not posi else -res


def is_valid(string):
    if string[0] != '-' and not '0' <= string[0] <= '9':
        return False
    if string[0] == '-' and (len(string) == 1 or string[1] == '0'):
        return False
    if string[0] == '0' and len(string) > 1:
        return False
    for i in string[1:]:
        if not '0' <= i <= '9':
            return False
    return True

# ----------------------------------------------------------------
# ----------------------------------------------------------------

def replace(str1, from1, to1):
    """
    2018-11-19
    替换字符串中连续出现的指定字符串
    ---
    给定三个字符串str1、from1和to1，已知from1字符串中无重复字符，
    把str中所有from1的子串全部替换成to1字符串，对连续出现from1的
    部分要求只替换一个to字符串，返回最终的结果字符串。
    """
    str2 = ''
    match = 0
    for index, value in enumerate(str1):
        if value == from1[match]:
            match += 1
            if match == len(from1):
                str2 += '0' * match
                match = 0
        else:
            if match != 0:
                str2 += str1[index - match:index]
            str2 += value
            match = 0

    res = ''
    for index, value in enumerate(str2):
        if value != '0':
            res += value
        else:
            if index == 0 or str2[index - 1] != '0':
                res += to1
    return res

# ----------------------------------------------------------------
# ----------------------------------------------------------------

def get_count_string(str1):
    """
    2018-11-20
    字符串的统计字符串
    ---
    给定一个字符串str1，返回str1的统计字符串。例如"aaabbaddffc"的
    统计字符串为"a_3_b_2_a_1_d_2_f_2_c_1"
    """

    if not str1 or not str1.strip():
        return ''

    res = ''
    num = 1
    for index in range(1, len(str1)):
        if str1[index] == str1[index - 1]:
            num += 1
        else:
            res += str1[index - 1] + '_' + str(num) + '_'
            num = 1

    res += str1[-1] + '_' + str(num)
    return res

# ----------------------------------------------------------------
# ----------------------------------------------------------------

def is_uniquel(chars):
    """
    2018-11-21
    判断字符数组中是否所有的字符都只出现过一次
    ---
    给定一个字符类型chars[]，判断chars中是否所有的字符都只出现过
    一次，请根据以下不同的两种要求实现两个函数
    1. 实现时间复杂度为O(N)的方法
    2. 在保证额外空间复杂度为O(1)的前提下，请实现时间复杂度尽量低
    的方法(暂未实现)
    """
    if len(chars) == 0:
        return False
    count = {}
    for chars in chars:
        if count.get(chars):
            return False
        else:
            count[chars] = 1
    return True

# ----------------------------------------------------------------
# ----------------------------------------------------------------

def get_index(strs, str1):
    """
    2018-11-22
    在有序但含有空的数组中查找字符串
    ---
    给定一个字符串数组strs，在strs中有些位置位''，但不为''的位置
    上，其字符串是按照字典顺序由小到大依次出现的。 再给定一个字
    符串str，请返回str在strs中出现的最左的位置。
    本地的解法尽可能使用了二分查找。
    """
    if not strs or not str1:
        return -1
    res = -1
    left = 0
    right = len(strs) - 1

    while left < right:
        mid = (left + right) / 2
        if not strs[mid] and strs[mid] == str1:
            right = mid - 1
            res = mid
        elif not strs[mid]:
            if strs[mid] > str1:
                left = mid + 1
            else:
                right = mid - 1
        else:
            i = mid - 1
            while not strs[i] and i >= left:
                i -= 1
            if i < left or strs[i] < left:
                left = mid + 1
            else:
                res = i if strs[i] == str1 else res
                right = i - 1
    return res
