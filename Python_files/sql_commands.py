from mysql.connector import connect, Error
from config import SQL_USER, SQL_PASS
from collections import defaultdict

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
    data = [i[0] for i in get_data_from_table('Users')]
    return data


def get_currencies():
    """returns dictionary with pairs CryptoSymbol: Value"""
    data = {i[0]: i[1] for i in get_data_from_table('Currencies')}
    return data


def get_user_has_currencies_raw():
    """returns list of pairs(tuples) of UserId: CryptoCurrency"""
    data = get_data_from_table('User_has_Currencies')
    return data


def get_user_has_currencies():
    """returns dictionary with pairs UserID: CryptoCurrencies"""
    data = get_data_from_table('User_has_Currencies')
    new_data = defaultdict(set)
    for user_id, symbol in data:
        new_data[user_id].add(symbol)
    return new_data
