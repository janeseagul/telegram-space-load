import os
import requests
import argparse

from load_main import get_file_ext, load_picture


def fetch_nasa_apod(count, nasa_api_key):
    params = {"api_key": nasa_api_key, "count": count}
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    for number, apod in enumerate(response.json()):
        if apod["media_type"] == "image":
            url = apod["url"]
            ext = get_file_ext(url)
            filepath = os.path.join("Images", f"nasa_apod_{number}{ext}")
            load_picture(url, filepath)


if __name__ == "__main__":
    os.makedirs("Images", exist_ok=True)
    nasa_api_key = os.environ['NASA_API']
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--count",
        default=40,
    )
    args = parser.parse_args()

    fetch_nasa_apod(args.count, nasa_api_key)
