import argparse
import os
import random
import time

from telegram.error import NetworkError

from send_images import send_photo

if __name__ == "__main__":
    token = os.environ['BOT_TOKEN']
    chat_id = os.environ['CHAT_ID']
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--images_dir_path",
        help="путь к директории с фотографиями",
        default="Images",
    )
    parser.add_argument(
        "-s",
        "--sleep_time",
        default=4,
        type=float,
    )
    args = parser.parse_args()
    sleep_time = args.sleep_time * 3600

    images_folders = []
    for address, dirs, files in os.walk(args.images_dir_path):
        for name in files:
            images_folders.append(os.path.join(address, name))

    while True:
        try:
            for images_folder in images_folders:
                send_photo(images_folder, chat_id, token)
                time.sleep(sleep_time)
            random.shuffle(images_folders)
        except NetworkError:
            print("Нет соединения.")
            time.sleep(2)
