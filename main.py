import os
from dotenv import load_dotenv
from spacex import fetch_spacex_last_launch
from apodnasa import get_apod

def main():
    load_dotenv()
    token = os.environ['NASA_TOKEN']

    fetch_spacex_last_launch()
    get_apod(token)


if __name__ == '__main__':
    main()