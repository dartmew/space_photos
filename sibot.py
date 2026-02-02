import argparse
import time
import json
from telegram import Bot
from dotenv import load_dotenv
import os
import random
from pathlib import Path


def load_settings(settings_file='bot_settings.json'):
    with open(settings_file, 'r', encoding='utf-8') as f:
        settings = json.load(f)
    print(f"Настройки загружены из {settings_file}")
    return settings

def send_picture(bot, chat_id, images_folder, image, caption):
    image_path = Path(images_folder) / image

    with open(image_path, 'rb') as photo_file:
        bot.send_photo(chat_id=chat_id, photo=photo_file, caption=caption)

def create_images_pool(images_folder, extensions):
    images_files = []

    for file in os.listdir(images_folder):
        file_lower = file.lower()
        if any(file_lower.endswith(ext) for ext in extensions):
            images_files.append(file)

    return images_files


def post_all_images(bot, chat_id, settings, interval):
    images_pool = create_images_pool(settings['images_folder'], settings['allowed_extensions'])
    
    while True:
        random.shuffle(images_pool)
        
        for image in images_pool:
            send_picture(bot, chat_id, settings['images_folder'], image, settings['caption_template'])
            time.sleep(interval)


def main():
    settings = load_settings()

    load_dotenv()
    token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']

    bot = Bot(token=token)

    parser = argparse.ArgumentParser(description='Post images in Telegram channel')
    parser.add_argument('image_name', nargs='?', default='',
                        help='Choose image to post (optional, default: none. If none bot will post all images)')
    parser.add_argument('interval_seconds', nargs='?', default=10, #14400
                        help='Posting interval in seconds (optional, default: 4 hours)')
    args = parser.parse_args()
    

    if args.image_name == '':
        post_all_images(bot, chat_id, settings, args.interval_seconds)
    else:
        send_picture(bot, chat_id, settings['images_folder'], args.image_name, settings['caption_template'])
        

if __name__ == '__main__':
    main()