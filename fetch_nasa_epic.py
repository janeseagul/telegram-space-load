import argparse
import datetime
import os

import requests
from dotenv import load_dotenv

from load_main import load_picture


def fetch_nasa_epic(nasa_api):
    params = {"api_key": nasa_api}
    response = requests.get(
        "https://api.nasa.gov/EPIC/api/natural/images", params=params
    )
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        image_name = image["image"]
        date = datetime.datetime.fromisoformat(image["date"])
        image_url = (
            f"https://api.nasa.gov/EPIC/archive/natural"
            f'/{date.strftime("%Y/%m/%d")}/png/{image_name}.png'
        )

        filename = os.path.join("Nasa_epic_images", f"nasa_epic_{number}.jpeg")
        load_picture(image_url, filename, params)


if __name__ == "__main__":
    os.makedirs("Nasa_epic_images")
    nasa_api = os.environ["NASA_API"]
    parser = argparse.ArgumentParser()
    parser.parse_args()

    fetch_nasa_epic(nasa_api)