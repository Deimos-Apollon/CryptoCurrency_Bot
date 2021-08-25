from mysql.connector import connect, Error
from config import SQL_USER, SQL_PASS


def set_connection_decorator(f):
    def set_connection_wrapper(*args, **kwargs):
        try:
            with connect(
                    host="localhost",
                    user=SQL_USER,
                    password=SQL_PASS,
                    database='CryptoIgor'
            ) as connection:
                print('decor works')
                return f(*args, **kwargs, connection=connection)
        except Error as e:
            print(f'Error setting connection calling {f.__name__}: {e}')
    return set_connection_wrapper


@set_connection_decorator
def add_new_user(user_id, connection):
    add_user_query = f'''
        INSERT INTO Users
        (idUser)
        VALUES ({user_id})
        '''
    with connection.cursor() as cursor:
        cursor.execute(add_user_query)
    connection.commit()


@set_connection_decorator
def get_data_from_table(table, connection):
    get_users_query = f'''
        SELECT * FROM {table};
        '''
    with connection.cursor() as cursor:
        cursor.execute(get_users_query)
        return cursor.fetchall()


def get_users():
    return get_data_from_table('Users')


def get_currencies():
    return get_data_from_table('Currencies')


def get_user_has_currencies():
    return get_data_from_table('User_has_Currencies')

