import requests
from config import SERVER_TOKEN
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from sql_commands import *


def add_user(user_id):
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


vk_session = vk_api.VkApi(token=SERVER_TOKEN)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
users = sql_get_users()
currencies = sql_get_currencies()
for event in longpoll.listen():
    if event.type == VkEventType.message_new:
        if event.text == r'\start':
            add_user(event.from_id)
        # как понять, какую криптовалюту попросил пользователь?
        # как корректно сравнить введенное название с названием в базе?
        # if event.text[:4] == r'\add':
        #     add_currency(event.from_id, event.text[4:])



