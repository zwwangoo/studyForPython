import mysql.connector
from contextlib import contextmanager
from functools import wraps
from retrying import retry


config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '12345',
    'database': 'demo',
    'charset': 'utf8'
}


class MysqlClient(object):

    def __init__(self, config):
        self.config = config

    @contextmanager
    def mysql_connector(self, cursor_dict=False):
        '''
        构建上下文
        '''
        try:
            conn = mysql.connector.connect(**self.config)

            if cursor_dict:
                cursor = conn.cursor(
                    cursor_class=mysql.connector.cursor.MySQLCursorDict)
            else:
                cursor = conn.cursor()

            yield cursor, conn
        except mysql.connector.Error as e:
            print(e)

        finally:
            if conn.is_connected():
                conn.close()


db = MysqlClient(config)


def query(cursor_dict=False):
    """ 执行sql 语句
    对被装饰的函数参数进行修改，传出mysql的connector和cursor

    :param cursor_dict: 查询结果为dict
    """
    def in_func(func):

        @wraps(func)
        @retry(stop_max_attempt_number=5, wait_random_min=100, wait_random_max=1000)
        def connect(*args, **kw):
            with db.mysql_connector(cursor_dict) as (cursor, conn):
                return func(cursor, conn, *args, **kw)

        return connect
    return in_func
