import os
import telegram
import fetch_nasa_apod

token = os.environ['BOT_API']
chat_id = os.environ['CHAT_ID']

bot = telegram.Bot(token=token)
bot.send_message(chat_id = chat_id, text = 'Привет! Хочешь получить фотографии с запуска SpaceX?')

bot.send_photo(chat_id=chat_id, photo = open('Nasa_epic_images/nasa_epic_1.jpeg', 'rb'))

