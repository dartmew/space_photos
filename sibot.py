from telegram import Bot
from dotenv import load_dotenv
import os


def send_picture():
    image_path = 'images/50291306061_2f9e350a85_o.jpg'


    with open(image_path, 'rb') as photo_file:
        bot.send_photo(chat_id=chat_id, photo=photo_file, caption='Классное фото - космос покоряет 🚀')

def make_image_pull(images_folder):
    images_files = []

    for file in os.listdir(images_folder):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            images_files.append(file)

    return images_files

def main():
    load_dotenv()
    token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    bot = Bot(token=token)
    images_folder = 'images'

    print(make_image_pull(images_folder))

if __name__ == '__main__':
    main()