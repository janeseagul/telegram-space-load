import argparse
import os
import random

from load_main import send_photos


def send_photo(bot_api_key, chat_id, file):
    if file:
        photo = file
    else:
        *__, last_photos = list(os.walk('Images'))
        *__, photos = last_photos
        photo = os.path.join('Images', random.choice(photos))
    send_photos(bot_api_key, chat_id, photo)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default=None)
    args = parser.parse_args()
    chat_id = os.environ['TG_CHAT_ID']
    bot_api_key = os.environ['BOT_API_KEY']
    send_photo(bot_api_key, chat_id, args.file)


if __name__ == '__main__':
    main()