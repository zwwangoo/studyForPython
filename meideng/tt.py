def get_month_days(y, m):
    leap_year = False
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        leap_year = True
    if m == 2:
        month_days = 28
        if leap_year:
            month_days = 29
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        month_days = 31
    else:
        month_days = 30
    return month_days


def get_order_days(y, m, d, length=1):
    days = get_month_days(y, m) - d
    for _ in range(1, length):
        y, m, d = get_deadline(y, m, d)
        days += get_month_days(y, m)
    over_y, over_m, over_d = get_deadline(y, m, d)
    days += over_d
    return days


def get_deadline(y, m, d, length=1):
    """
    给定订购的年月日，和时长，返回订单到期日
    :param y: 订购的年份
    :param m: 订购的月份
    :param d: 订购的日
    :param length: 订购的时长，默认为1个月,为任意自然数
    :return: 到期的年月日
    """
    
    
    y += (m + length) // 12
    m = (m + length) % 12
    
    month_day = get_month_days(y, m) 

    if d > month_day:
        d = month_day # d = 28 
            
    return y, m, d
