from utils import download_file
import requests


def fetch_spacex_last_launch():
    folder = 'images'
    url = 'https://api.spacexdata.com/v5/launches/{}'
    response = requests.get(url.format('latest'))
    response.raise_for_status()
    links = response.json().get('links').get('flickr').get('original')

    if not links:
        response = requests.get(url.format('5eb87d47ffd86e000604b38a'))
        response.raise_for_status()
        links = response.json().get('links').get('flickr').get('original')

        for link in links:
            download_file(link, folder)
    else:
        for link in links:
            download_file(link, folder)
