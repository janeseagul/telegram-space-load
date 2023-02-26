import argparse
import os
import random

from load_main import send_picture


def send_photo(bot_api_key, chat_id, file):
    if file:
        photo = file
    else:
        *__, last_photos = list(os.walk('Images'))
        *__, photos = last_photos
        photo = os.path.join('Images', random.choice(photos))
    send_picture(bot_api_key, chat_id, photo)


def main():
    parser = argparse.ArgumentParser(description='Отправка выбранного изображения в чат телеграм')
    parser.add_argument(
        "-f",
        "--file",
        help='Название файла с изображением в виде {Название картинки}{формат}.',
        default=None
    )

    args = parser.parse_args()
    chat_id = os.environ['TG_CHAT_ID']
    bot_api_key = os.environ['BOT_API_KEY']
    send_photo(bot_api_key, chat_id, args.file)


if __name__ == '__main__':
    main()