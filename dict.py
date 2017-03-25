# -*- coding: utf-8 -*-

import config
import telegram
from subprocess import Popen, PIPE
import re

bot = telegram.Bot(token=config.TOKEN)

def dictionary(x):
    if '/test' in config.messages[-1]:
        bot.sendMessage(chat_id=config.chat_id, text="Слушай, хватит уже!")
    elif '/hellow' in config.messages[-1]:
        bot.sendMessage(chat_id=config.chat_id, text="Привет, че!")
    else:
        command = x[1:]
        stdout = str(Popen(command, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
        bot.sendMessage(chat_id=config.chat_id, text=stdout.replace('reboot','lol').replace('shutdown','nax'))