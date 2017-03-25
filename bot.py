# -*- coding: utf-8 -*-

import dict
import telegram
import config
import func

bot = telegram.Bot(token=config.TOKEN)
updates = bot.getUpdates()
func.get_last_id(updates)
count = config.messages_id[-1]

while config.last:
    updates = bot.getUpdates()
    func.get_last_id(updates)
    if count != config.messages_id[-1]:
        func.get_last(updates)
        config.last = False
        dict.dictionary(config.messages[-1])




