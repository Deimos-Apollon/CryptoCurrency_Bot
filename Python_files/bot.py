import json
import vk_api
import requests
from config import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from sql_commands import *

if __name__ == "__main__":
    print(sql_get_users())
    print(sql_get_currencies())
    print(sql_get_user_has_currencies())
    print(sql_get_user_has_currencies_raw())