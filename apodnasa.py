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

    data = response.json()

    for element in data:
        download_file(element['hdurl'])


def main():
    load_dotenv()
    token = os.environ['NASA_TOKEN']

    parser = argparse.ArgumentParser(description='Download pictures of day from NASA')
    parser.add_argument('count', nargs='?', default='5',
                        help='Count of pictures to download (optional, default: 5)')
    args = parser.parse_args()

    try:
        get_apod(token, int(args.count))
    except requests.exceptions.HTTPError as e:
        print(f'HTTPError: {e}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()