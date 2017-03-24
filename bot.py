# -*- coding: utf-8 -*-

import dict
import telegram
import config
import func

bot = telegram.Bot(token=config.TOKEN)
updates = bot.getUpdates()
count = len(updates)

while config.last:
    updates = bot.getUpdates()
    if count < len(updates):
        func.get_last(updates)
        config.last = False
        dict.dictionary(config.messages[-1])





