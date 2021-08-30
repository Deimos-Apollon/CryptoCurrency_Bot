import json
import vk_api
import requests
from commands import *
from config import *
from vk_api.longpoll import VkLongPoll, VkEventType
from sql_commands import *


def bot_listen(longpoll, vk, users, currencies):
    for event in longpoll.listen():
        if event.type == VkEventType.message_new:
            text = list(event.text.split())
            if text[0] == 'start':
                add_user(event.from_id, vk, users)
            elif text[0] == 'add':
                pass


def bot_start():
    vk_session = vk_api.VkApi(token=SERVER_TOKEN)
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    users = sql_get_users()
    currencies = sql_get_currencies()
    bot_listen(longpoll, vk, users, currencies)