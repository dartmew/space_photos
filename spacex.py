from utils import download_file
import requests
import argparse


def get_spacex_links(launch_id):
    """Получает ссылки на фото запуска SpaceX"""
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    links = data.get('links', {}).get('flickr', {}).get('original', [])
    return links


def download_spacex_photos(launch_id='latest', folder='images'):
    links = get_spacex_links(launch_id)

    if not links and launch_id != 'latest':
        links = get_spacex_links('latest')
    
    for link in links:
        download_file(link, folder)


def main():
    parser = argparse.ArgumentParser(description='Download images from spacex')
    parser.add_argument('launch_id', nargs='?', default='latest',
                        help='SpaceX launch ID (optional, default: latest)')
    args = parser.parse_args()
    download_spacex_photos(args.launch_id)

if __name__ == '__main__':
    main()