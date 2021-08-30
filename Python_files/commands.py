from sql_commands import *


def add_user(user_id, vk, users):
    if (user_id not in users) and len(users) < 10:
        sql_add_new_user(user_id)
        users.append(user_id)
        vk.messages.send(
            user_id=user_id,
            message='Добро пожаловать!',
            random_id=0)
    else:
        vk.messages.send(
            user_id=user_id,
            message='Ошибка :(',
            random_id=0)
