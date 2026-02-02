import os
from urllib.parse import urlparse, unquote
import requests
from pathlib import Path


def get_file_extension(url):
    return urlparse(url).path.split('.')[-1]


def get_file_name(url):
    parsed = urlparse(url)
    decoded = unquote(parsed.path)
    return os.path.basename(decoded)


def download_file(url, download_folder='images', headers=None):
    if headers is None:
        headers = {}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    Path(download_folder).mkdir(parents=True, exist_ok=True)
    download_path = Path(download_folder) / get_file_name(url)

    with open(download_path, 'wb') as file:
        file.write(response.content)
    
    print(f'Downloaded {file.name}')