# pip install Pillow, pip install openpyxl, pip install fake-headers

import json
from datetime import datetime, timedelta

from tools.create_subfolder import create_directory
from tools.downloader import image_downloader
from tools.get_file_name import ImageNamer

from tools.get_html import get_html
from tools.lenta_ru_time import lenta_ru_time_converter
from tools.system_notification import notification


def main():
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    folder = create_directory('Kommersant/LentaRU')
    number = 10

    while True:
        url = f"https://lenta.ru/search/v2/process?from=0&size={number}" \
              f"&sort=2&title_only=0&domain=1&modified,format=yyyy-MM-dd&query=фото Коммерсантъ"
        result = json.loads(get_html(url))
        count = 0
        for i in result['matches']:
            if lenta_ru_time_converter(i['pubdate']) == yesterday:  # today:
                count += 1
                photograph = i['text'].split('/ Коммерсантъ')[0][6:].strip()

                # если под фото нед подписи и взята первая строка текста, то пропускаем снимок
                if len(photograph) < 25:
                    image_url = i['image_url']
                    print(photograph, image_url, lenta_ru_time_converter(i['pubdate']))

                    image_name = f"{ImageNamer().file_name(image_url)}_{photograph}.JPG"

                    image_downloader(image_url, folder, image_name)

        if count < 10:
            notification("LentaRu completed")
            break
        number += 10


if __name__ == '__main__':
    main()
