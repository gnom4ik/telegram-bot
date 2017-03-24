import config
import telegram

bot = telegram.Bot(token=config.TOKEN)

def dictionary(x):
    if config.messages[-1] == '/test':
        bot.sendMessage(chat_id=config.chat_id, text="Слушай, хватит уже!")
    elif config.messages[-1] == '/hellow':
        bot.sendMessage(chat_id=config.chat_id, text="Привет, че!")