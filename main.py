import os
import argparse
import random
import time
from typing import List

from load_main import send_picture

if __name__ == '__main__':
    bot_api_key = os.environ['BOT_API_KEY']
    chat_id = os.environ['TG_CHAT_ID']
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--images_path",
        help='Название директории с изображениями',
        default="images"
    )
    parser.add_argument(
        "-s",
        "--sleep_time",
        help='Время задержки отправки изображений в секундах',
        default=4,
        type=float
    )
    args = parser.parse_args()
    sleep_time = args.sleep_time * 3600

    images_paths: = []

    for address, dirs, files in os.walk(args.images_path):
        for name in files:
            images_paths.append(os.path.join(address, name))

    while True:
        for images_path in images_paths:
            send_picture(bot_api_key, chat_id, images_path)
            time.sleep(sleep_time)
        random.shuffle(images_paths)