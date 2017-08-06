# -*- coding: utf-8 -*-
import xlrd
import MySQLdb
# Open the workbook and define the worksheet
book = xlrd.open_workbook("shangwang.xlsx")
sheet = book.sheet_by_index(0)

# 建立一个MySQL连接
database = MySQLdb.connect(
    host="localhost", user="root", passwd="123456", db="zhi")

# 获得游标对象, 用于逐行遍历数据库数据
cursor = database.cursor()

# 创建插入SQL语句
query = "INSERT INTO we (accounts,passwd, name) VALUES (%s, %s, %s)"

# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题
for r in range(1, sheet.nrows):
    accounts = sheet.cell(r, 0).value
    passwd = sheet.cell(r, 1).value
    name = sheet.cell(r, 2).value.encode('UTF-8')
    values = (accounts, passwd, name)

    # # 执行sql语句
    cursor.execute(query, values)

# 关闭游标
cursor.close()

# 提交
database.commit()

# 关闭数据库连接
database.close()

# 打印结果
print ""
print "Done! "
print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print "我刚导入了 %s 列 and %s 行数据到MySQL!" % (columns, rows)
