# pip install Pillow, pip install openpyxl, pip install fake-headers
import os
import requests
import json
from openpyxl.drawing.image import Image
from datetime import datetime, timedelta

from tools.create_subfolder import create_directory
from tools.get_html import get_html
from tools.lenta_ru_time import lenta_ru_time_converter

yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
report_folder = 'Users/Documents/Kommersant/LentaRU'


def notification(message):
    title = "Готово"
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)


def make_subfolder(photograf):
    folder = f"{report_folder}/{yesterday}/{photograf}"
    os.makedirs(folder, exist_ok=True)
    return folder


def download_image(folder, image_url, photograf, yesterday):
    r = requests.get(image_url)
    image_name = f"{yesterday}_{photograf}_{image_url.split('/')[-1]}"
    with open(f"{folder}/{image_name}", 'wb') as download_file:
        for chunk in r.iter_content(9000):
            download_file.write(chunk)
    return f"{folder}/{image_name}"


def main():
    number = 10

    while True:
        url = f"https://lenta.ru/search/v2/process?from=0&size={number}" \
              f"&sort=2&title_only=0&domain=1&modified,format=yyyy-MM-dd&query=фото Коммерсантъ"
        rezult = json.loads(get_html(url))
        count = 0
        for i in rezult['matches']:
            if lenta_ru_time_converter(i['pubdate']) == yesterday:  # today:
                count += 1
                photograf = i['text'].split('/ Коммерсантъ')[0][6:].strip()

                # если под фото нед подписи и взята первая строка текста, то пропускаем снимок
                if len(photograf) < 25:
                    image_url = i['image_url']
                    # ws.row_dimensions[count].height = 100  # задаю высоту столбца
                    print(photograf, image_url, lenta_ru_time_converter(i['pubdate']))

                    # folder = make_subfolder(photograf)
                    folder = create_directory(f'Kommersant/LentaRU')
                    image_path = download_image(folder, image_url, photograf, yesterday)

                    img = Image(image_path)
                    resize_height = img.height // 3  # уменьшая рарешение в два раза
                    resize_width = img.width // 3  # уменьшая рарешение в два раза

                    img.width = resize_width  # устанавливаю размер превью
                    img.height = resize_height  # устанавливаю размер превью

        if count < 10:
            notification("LentaRu completed")
            break
        number += 10


if __name__ == '__main__':
    main()
