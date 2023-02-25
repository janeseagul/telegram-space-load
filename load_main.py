from os.path import splitext
from urllib.parse import urlparse
import telegram

import requests


def load_picture(url, filename, params=None):
	response = requests.get(url, params=params)
	response.raise_for_status()
	with open(filename, "wb") as file:
		file.write(response.content)


def get_file_ext(url):
	path = urlparse(url).path
	file_path, extension = splitext(path)
	return extension


def send_photos(bot_api_key, chat_id, photo):
	bot = telegram.Bot(token=bot_api_key)
	with open(photo, 'rb') as image:
		bot.send_photo(chat_id=chat_id, photo=image)