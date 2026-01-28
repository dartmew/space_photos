import requests
from utils import download_file


def get_apod(api_key, count=5):
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
