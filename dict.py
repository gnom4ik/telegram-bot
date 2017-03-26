# -*- coding: utf-8 -*-

import config
import telegram
from subprocess import Popen, PIPE
import re

bot = telegram.Bot(token=config.TOKEN)

def dictionary(x):
    if '/test' in config.messages[-1]:
        bot.sendMessage(chat_id=config.chat_id, text="Слушай, хватит уже!")
    elif '/start' in config.messages[-1]:
        bot.sendMessage(chat_id=config.chat_id, text="Привет, че!")
    elif '/help' or '/?' in config.messages[-1]:
        bot.sendMessage(chat_id=config.chat_id, text="Я принимаю команды только используя /. Команды выведены выше.")
    elif '/hostname' in config.messages[-1]:
        command = 'hostname'
        stdout = str(Popen(command, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
        bot.sendMessage(chat_id=config.chat_id, text=stdout[2:-3])
    elif '/date' in config.messages[-1]:
        command = 'date "+%H:%m %d-%m-%Y"'
        stdout = str(Popen(command, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
        bot.sendMessage(chat_id=config.chat_id, text=stdout[2:-3])