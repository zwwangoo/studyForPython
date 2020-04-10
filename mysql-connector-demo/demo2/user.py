from mysql_client_base import query


@query(True)
def get_user_info(cursor, conn):
    cursor.execute('select name from user')
    return cursor.fetchall()


print(get_user_info())
