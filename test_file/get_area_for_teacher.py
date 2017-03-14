# coding: UTF-8
# -*- coding: utf-8 -*-
'''
分析获取教师的居住地和临近乘车点，绘制最优乘车路线
'''
import csv

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
        writer.writerows(info)
    except Exception as err:
        print err
    finally:
        conn.close()

if __name__ == '__main__':
    update_teacher_new_arae()