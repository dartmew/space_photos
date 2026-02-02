import requests
from utils import download_file
import argparse
from dotenv import load_dotenv
import os


def get_apod(api_key, count):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': count
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    apod_items = response.json()

    for apod_item in apod_items:
        download_file(apod_item['url'])


def main():
    load_dotenv()
    token = os.environ['NASA_TOKEN']

    parser = argparse.ArgumentParser(description='Download pictures of day from NASA')
    parser.add_argument('count', nargs='?', type=int, default=5,
                        help='Count of pictures to download (optional, default: 5)')
    args = parser.parse_args()
    get_apod(token, args.count)


if __name__ == '__main__':
    main()