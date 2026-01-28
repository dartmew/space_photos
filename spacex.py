from utils import download_file
import requests
import argparse


def fetch_spacex_last_launch(launch_id):
    folder = 'images'
    url = 'https://api.spacexdata.com/v5/launches/{}'
    response = requests.get(url.format(launch_id))
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


def main():
    parser = argparse.ArgumentParser(description='Download images from spacex')
    parser.add_argument('launch_id', nargs='?', default='latest',
                        help='SpaceX launch ID (optional, default: latest)')
    args = parser.parse_args()

    try:
        fetch_spacex_last_launch(args.launch_id)
    except requests.exceptions.HTTPError as e:
        print(f'HTTPError: {e}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()