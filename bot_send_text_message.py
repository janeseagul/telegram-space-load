import os
import telegram
token = os.environ['BOT_API']
chat_id = os.environ['CHAT_ID']

bot = telegram.Bot(token=token)
bot.send_message(chat_id = chat_id, text = 'Привет! Хочешь получить фотографии с запуска SpaceX?')

