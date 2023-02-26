import datetime
import os

import requests

from load_main import load_picture


def fetch_nasa_epic(nasa_api_key):
    params = {"api_key": nasa_api_key}
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

        filepath = os.path.join("Images", f"nasa_epic_{number}.jpeg")
        load_picture(image_url, filepath, params)


if __name__ == "__main__":
    os.makedirs("Images", exist_ok=True)
    nasa_api_key = os.environ['NASA_KEY']

    fetch_nasa_epic(nasa_api_key)