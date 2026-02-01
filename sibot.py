import argparse
import time
import json
from telegram import Bot
from dotenv import load_dotenv
import os
import random


def load_settings(settings_file='bot_settings.json'):
    with open(settings_file, 'r', encoding='utf-8') as f:
        settings = json.load(f)
    print(f"Настройки загружены из {settings_file}")
    return settings

def send_picture(bot, chat_id, images_folder, image, caption):
    image_path = f'{images_folder}/{image}'

    with open(image_path, 'rb') as photo_file:
        bot.send_photo(chat_id=chat_id, photo=photo_file, caption=caption)

def make_images_pull(images_folder, extensions):
    images_files = []

    for file in os.listdir(images_folder):
        file_lower = file.lower()
        if any(file_lower.endswith(ext) for ext in extensions):
            images_files.append(file)

    return images_files

def shuffle_images_pull(images_pull):
    random.seed()
    random.shuffle(images_pull)

def post_images_from_pull(bot, chat_id, settings, images_pull, interval):
    images_folder = settings['images_folder']
    caption = settings['caption_template']
    for image in images_pull:
        send_picture(bot, chat_id, images_folder, image, caption)
        time.sleep(interval)

def single_post(image_name):
    if image_name == '':
        return True
    else:
        return False

def main():
    settings = load_settings()

    load_dotenv()
    token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']

    bot = Bot(token=token)
    images_folder = settings['images_folder']

    parser = argparse.ArgumentParser(description='Post images in Telegram channel')
    parser.add_argument('image_name', nargs='?', default='',
                        help='Choose image to post (optional, default: none. If none bot will post all images)')
    parser.add_argument('interval_seconds', nargs='?', default=14400,
                        help='Posting interval in seconds (optional, default: 4 hours)')
    args = parser.parse_args()
    extensions = settings['allowed_extensions']

    if single_post(args.image_name):
        send_picture(bot, chat_id, settings['image_folder'], args.image_name, settings['caption_template'])
    else:
        images_pull = make_images_pull(images_folder, extensions)

        while(True):
            shuffle_images_pull(images_pull)
            post_images_from_pull(bot, chat_id, settings, images_pull, args.interval_seconds)
            print('new round')

if __name__ == '__main__':
    main()