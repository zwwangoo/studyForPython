# coding: UTF-8
# -*- coding: utf-8 -*-
'''
分析获取教师的居住地和临近乘车点，绘制最优乘车路线
'''
import csv
import sys

import MySQLdb


def update_teacher_new_arae():

    conn = MySQLdb.connect(
        host='127.0.0.1',
        db='busBook',
        user='root',
        passwd='123456',
        port=3306
    )

    try:
        cursor = conn.cursor()
        select_teacher = """
            SELECT
                staffNum, name, departmentid, route, street, region, commubity
            FROM
                staff
            WHERE
                route IS NOT NULL OR street IS NOT NULL
            """
        set_sql = cursor.execute(select_teacher)
        info = cursor.fetchmany(set_sql)
        List = []
        infofile = file("info.csv", 'wb+')
        writer = csv.writer(infofile)
        writer.writerow(['工号', '姓名', '部门编号', '道', '路', '区', '小区'])
        for i in info:
            List.append(i)
        writer.writerows(info)  # 导出的csv编码格式不正确
    except Exception as err:
        print err
    finally:
        conn.close()

import  re
import jieba

def str_split(info_str):
    ''' 分词处理 '''
    # for _ in range(2):
    # notEffectiveChar = "1234567890abcdefghijklmnopqrstuvwxyz"
    # effectiveForInfo = []
    # str_info = info_str.split("\"")  # 将该行数据以 “ 分割
    # # if len(str_info) > 4:
    # for i in str_info:
    #     # print len(i),
    #     if len(i) > 4:  # 为有效字符  一个汉字的有效长度为3
    #         k = ""
    #         for j in i:
    #
    #             if j not in notEffectiveChar:
    #                 k += j
    #         effectiveForInfo.append(k)
    # if len(effectiveForInfo) > 4:
    #     return effectiveForInfo[1:]
    # else:
    #     return None
    strlist = re.findall('[\x80-\xff]+', info_str)
    effectiveForInfo = ''.join(strlist)
    if len(effectiveForInfo) > 9:
        return effectiveForInfo
    else:
        return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "文件名错误"
        raise SystemExit(1)

    f = open(sys.argv[1])
    info = f.readlines()
    for i in info:
        effectiveForInfo = str_split(i)
        if effectiveForInfo:
            info_str_cut = jieba.cut(effectiveForInfo)
            print ", ".join(info_str_cut)
