from sql_commands import *


def add_user(user_id, vk, users, users_has_currencies):
    if user_id in users:
        vk.messages.send(
            user_id=user_id,
            message='Ошибка: Вы уже внесены в базу данных!',
            random_id=0)
    elif len(users) >= 10:

        vk.messages.send(
            user_id=user_id,
            message='Ошибка: места нет!',
            random_id=0)
    else:
        sql_add_new_user(user_id)
        users.append(user_id)
        vk.messages.send(
            user_id=user_id,
            message='Добро пожаловать!',
            random_id=0)


def add_currency_to_user(currency, user_id, currencies, users_has_currencies):
    if currency not in currencies:
        sql_add_new_currency(currency)
        currencies[currency] = -1
    users_has_currencies[user_id].add(currency)
    sql_add_user_has_currencies(user_id, currency)
