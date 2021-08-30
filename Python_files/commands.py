import requests
from config import SERVER_TOKEN
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from sql_commands import *


def add_user(user_id, vk, users):
    if (user_id not in users) and len(users < 10):
        sql_add_new_user(user_id)
        users.append(user_id)
        vk.messages.send(
            user_id=user_id,
            message='Добро пожаловать!')
    else:
        vk.messages.send(
            user_id=user_id,
            message='Ошибка :(')
