import argparse
import os

import telegram


def send_photo(images_folders, chat_id, token):
    bot = telegram.Bot(token=token)
    with open(images_folders, "rb") as image:
        bot.send_photo(chat_id=chat_id, photo=image)


if __name__ == "__main__":
    token = os.environ['BOT_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--images_folder"
    )
    parser.add_argument(
        "-id",
        "--chat_id",
	)
    args = parser.parse_args()

    send_photo_to_chat(args.images_folder, args.chat_id, token)