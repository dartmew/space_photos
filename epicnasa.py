import pprint
import requests
from utils import download_file


def get_epic(api_key):
    params = {
        'api_key': api_key
    }
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    pprint(data)
