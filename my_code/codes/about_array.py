# coding: utf-8
# ----------------------------------------------------------------
# ----------------------------------------------------------------


def spiral_order_print(matrix):
    """
    转圈打印矩阵。
    ---
    例如：
    1  2  3  4
    5  6  7  8
    9  10 11 12
    13 14 15 16
    打印结果为 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 10, 5, 6, 7
    """
    tr = tc = 0
    dr = len(matrix) - 1
    result = []
    if dr < 0:
        return result
    else:
        dc = len(matrix[0]) - 1
    while tr <= dr and tc <= dc:
        print_edge(matrix, tr, tc, dr, dc, result)
        tr += 1
        tc += 1
        dr -= 1
        dc -= 1
    return result


def print_edge(matrix, tr, tc, dr, dc, result):

    if tr == dr:  # 单行
        for i in range(tc, dc + 1):
            result.append(matrix[tr][i])
    elif tc == dc:  # 单列
        for j in range(tr, dr + 1):
            result.append(matrix[j][tc])
    else:
        cur_r = tr
        cur_c = tc
        while cur_c != dc:  # 打印最上行
            result.append(matrix[tr][cur_c])
            cur_c += 1
        while cur_r != dr:  # 打印最右行
            result.append(matrix[cur_r][dc])
            cur_r += 1
        while cur_c != tc:  # 打印最下行
            result.append(matrix[dr][cur_c])
            cur_c -= 1
        while cur_r != tr:  # 打印最左行
            result.append(matrix[cur_r][tc])
            cur_r -= 1


# ----------------------------------------------------------------
# ----------------------------------------------------------------


def rotate(matrix):
    """
    将正方形矩阵顺时针旋转九十度。
    ---
    例如：
    1  2  3  4
    5  6  7  8
    9  10 11 12
    13 14 15 16
    顺时针旋转九十度后：
    13 9  5  1
    14 10 6  2
    15 11 7  3
    16 12 8  4
    """
    tr = tc = 0
    dr = len(matrix) - 1
    dc = len(matrix[0]) - 1
    while tr < dr:
        rotate_edge(matrix, tr, tc, dr, dc)
        tr += 1
        tc += 1
        dr -= 1
        dc -= 1
    return matrix


def rotate_edge(matrix, tr, tc, dr, dc):

    times = dc - tc
    for i in range(times):
        tmp = matrix[tr][tc + i]
        matrix[tr][tc + i] = matrix[dr - i][tc]
        matrix[dr - i][tc] = matrix[dr][dc - i]
        matrix[dr][dc - i] = matrix[tr + i][dc]
        matrix[tr + i][dc] = tmp


# ----------------------------------------------------------------
# ----------------------------------------------------------------

def print_matrix_zig_zag(matrix):
    """
    之字打印矩阵。
    ---
    例如：
    1  2  3  4
    5  6  7  8
    9  10 11 12
    13 14 15 16
    打印结果为：
    1 2 5 9 6 3 4 7 10 13 14 11 12 15 16
    """
    tr = tc = 0
    dr = dc = 0
    end_r = len(matrix) - 1
    end_c = len(matrix[0]) - 1
    result = []
    from_up = False
    while tr != end_r + 1:
        print_level(matrix, tr, tc, dr, dc, end_c, from_up, result)
        tr = tr + 1 if tc == end_c else tr
        tc = tc if tc == end_c else tc + 1
        dc = dc + 1 if dr == end_r else dc
        dr = dr if dr == end_r else dr + 1
        from_up = not from_up
    return result


def print_level(matrix, tr, tc, dr, dc, end_c, from_up, result):
    if from_up:
        while tr != dr + 1:
            result.append(matrix[tr][tc])
            tr += 1
            tc -= 1
    else:
        while dr != tr - 1 and dc <= end_c:
            result.append(matrix[dr][dc])
            dr -= 1
            dc += 1
