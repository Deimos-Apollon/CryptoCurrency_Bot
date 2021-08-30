import json
import vk_api
import requests
from commands import *
from config import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from sql_commands import *


def bot_listen(longpoll, vk, users, currencies):
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            text = event.object['message']['text'].split()
            print(text, text[0])
            if text[0] == 'start':
                add_user(event.object['message']['from_id'], vk, users)
            elif text[0] == 'add':
                pass


def bot_start():
    vk_session = vk_api.VkApi(token=SERVER_TOKEN)
    longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)
    vk = vk_session.get_api()
    users = sql_get_users()
    currencies = sql_get_currencies()
    bot_listen(longpoll, vk, users, currencies)