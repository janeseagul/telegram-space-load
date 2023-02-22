import os
import requests
import argparse

from urllib.parse import urlparse
from os.path import splitext

from load_main import get_file_ext, load_picture


def fetch_nasa_apod(count, nasa_api):
    params = {"api_key": nasa_api, "count": count}
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    for number, apod in enumerate(response.json()):
        if apod["media_type"] == "image":
            url = apod["url"]
            ext = get_file_ext(url)
            filename = os.path.join("Nasa_apod_images", f"nasa_apod_{number}{ext}")
            load_picture(url, filename)


if __name__ == "__main__":
    os.makedirs("Nasa_apod_images")
    nasa_api = os.environ['NASA_API']
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--count",
        default=30,
    )
    args = parser.parse_args()

    fetch_nasa_apod(args.count, nasa_api)
