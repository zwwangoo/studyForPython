# -*- coding: utf-8 -*-
import MySQLdb


# 建立一个MySQL连接
database = MySQLdb.connect(
    host="10.16.155.241",  # 主机
    port=5002,  # 端口号
    user="mysqlroot",  # 用户名
    passwd="chuangxin2624",  # 登录密码
    db="busBook"  # 数据库名
)


# 获得游标对象, 用于逐行遍历数据库数据
cursor = database.cursor()
# 创建插入SQL语句
select_sql = "SELECT * FROM raserveinfor WHERE "
set_sql = cursor.execute(select_sql)
# aa = cursor.fetchone()
# 获取所有的预约信息
info = cursor.fetchmany(set_sql)

insert_sql = "INSERT INTO oldraserveinfor VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
delete_sql = "DELETE FROM raserveinfor WHERE reserveinforid = %s"
for a in info:
    cursor.execute(insert_sql, (a[0], a[1], a[2], a[3], a[4], a[
                   5], a[6], a[7], a[8], a[9], a[10], a[11], a[12]))
    cursor.execute(delete_sql, a[0])
    print "复制成功"

# 关闭游标
cursor.close()
database.commit()
# 关闭数据库连接
database.close()

print "数据库连接成功！"
