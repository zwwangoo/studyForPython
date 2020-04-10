import mysql.connector
from functools import wraps
from contextlib import contextmanager

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'demo',
    'charset': 'utf8'
}


class MysqlClient(object):

    def __init__(self, config):
        self.config = config

    @contextmanager
    def mysql_connector(self, cursor_dict=False):

        try:
            conn = mysql.connector.connect(**config)

            if cursor_dict:
                cursor = conn.cursor(
                    cursor_class=mysql.connector.cursor.MySQLCursorDict)
            else:
                cursor = conn.cursor()

            yield cursor, conn
        except mysql.connector.Error as e:
            print(e)

        finally:
            conn.close()


db = MysqlClient(config)


def query(cursor_dict=False):
    """
    sql 执行语句，对被装饰的函数参数进行修改，传出mysql的connector和cursor
    """
    def in_func(func):

        @wraps(func)
        def _in(*args, **kw):
            with db.mysql_connector(cursor_dict) as (cursor, conn):
                return func(cursor, conn, *args, **kw)

        return _in
    return in_func


@query(True)
def get_user_info(cursor, conn):
    cursor.execute('select name, age from user')
    results = cursor.fetchall()
    print(results)


@query()
def insert_user(cursor, conn):
    cursor.execute('insert into user(name, age) values ("hex", 12)')
    conn.commit()
    return cursor.lastrowid


# get_user_info()
print(insert_user())
get_user_info()
print('-----')
get_user_info()


# 创建表user
# with mysql_connector() as conn:
#     cursor = conn.cursor()
#     create_database = '''
#       create table user
#       (
#         id int auto_increment,
#         name varchar(255) null,
#         age int null,
#         constraint user_pk
#         primary key (id)
#       )
#     '''
#     cursor.execute(create_database)
#     conn.commit()

# 查询

# with mysql_connector() as conn:
#     # cursor = conn.cursor()
#     # 设定查询结果返回字典
#     cursor = conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
#     sql = 'select name, age from user limit 2'
#     cursor.execute(sql)
#
#     # 获取列名
#     columns = cursor.column_names
#     # 获取所有的结果
#     results = cursor.fetchall()
#     # 获取一个结果
#     # results = cursor.fetchone()
#     print(columns)
#     print(results)
#
# with mysql_connector() as conn:
#     cursor = conn.cursor()
#     sql = 'select id, name, age from user limit 2'
#     cursor.execute(sql)
#
#     # 列出查询的信息
#     for id, name, age in cursor:
#         print(id, name, age)
#
#
# # 新增数据
#
# with mysql_connector() as conn:
#     cursor = conn.cursor()
#
#     # 占位符方式
#     insert = '''
#     insert into user
#       (name, age)
#     values
#       (%(name)s, %(age)s)
#     '''
#     cursor.execute(insert, {'name': 'San', 'age': 12})
#
#     conn.commit()
#     # 获取刚刚插入数据的id
#     lastrowid = cursor.lastrowid
#     print(lastrowid)
#
# # 批量插入
#
# with mysql_connector() as conn:
#
#     cursor = conn.cursor()
#     insertmany = '''
#     insert into user
#       (name, age)
#     values
#       (%(name)s, %(age)s)
#     '''
#     data = [
#         {'name': 'Tom', 'age': 1},
#         {'name': 'Jom', 'age': 19}
#     ]
#     # 批量执行插入语句
#     cursor.executemany(insertmany, data)
#
#     conn.commit()
