import os
import requests
import argparse

from load_main import load_picture


def fetch_spacex_photos(launch_id):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    images_urls = response.json()["links"]["flickr"]["original"]
    for number, image_url in enumerate(images_urls):
        filepath = os.path.join("Images", f"spacex_{number}.jpeg")
        load_picture(image_url, filepath)


if __name__ == "__main__":
    os.makedirs("Images", exist_ok=True)
    parser = argparse.ArgumentParser(description='Загрузка фотографий с запусков SpaceX')
    parser.add_argument(
        "-i",
        "--launch_id",
        help='Id запуска SpaceX, для которого нужно загрузить фотографии'
        default="latest"
    )
    args = parser.parse_args()

    fetch_spacex_photos(args.launch_id)