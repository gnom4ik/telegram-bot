# -*- coding: utf-8 -*-

import dict
import telegram
import config
import func
import time

bot = telegram.Bot(token=config.TOKEN)
updates = bot.getUpdates(offset=config.offset)
func.get_last_id(updates)

while config.last:
    count = config.messages_id[-1]
    updates = bot.getUpdates(offset=config.offset)
    func.get_last_id(updates)
    if count != config.messages_id[-1]:
        func.get_last(updates)
        #config.last = False
        dict.dictionary(config.messages[-1])
        config.offset = count
    if config.offset == count:
        time.sleep(5)
        print(config.offset, count)
    else:
        config.offset += 1
        time.sleep(5)



