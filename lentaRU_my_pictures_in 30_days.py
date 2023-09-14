import requests
import json
import time
import datetime
import os
from datetime import datetime, timedelta

from get_file_name import file_name
from get_html import get_html


def lenta_ru_time_converter(lenta_ru_time):
    return datetime.strptime(time.ctime(lenta_ru_time), '%a %b %d %H:%M:%S %Y').strftime('%Y-%m-%d')


def main():
    for day_shift in range(2):

        publication_day = (datetime.now() - timedelta(days=day_shift)).strftime("%Y-%m-%d")

        autor = "Фото: Евгений Павленко / «Коммерсантъ»"

        url = f"https://lenta.ru/search/v2/process?from={str(day_shift)}" \
              f"&size=10&sort=2&title_only=0&domain=1&modified,format=yyyy-MM-dd&query={autor}"
        rezult = json.loads(get_html(url))

        for i in rezult['matches']:
            # if lenta_ru_time_converter(i['pubdate']) == publication_day:
            print(i['image_url'])
            os.makedirs(f"Евгений Павленко", exist_ok=True)
            filename = f"{file_name(i['image_url'])}.JPG"
            r = requests.get(i['image_url'])
            with open(f'Евгений Павленко/{filename}', 'wb') as download_file:
                for chunk in r.iter_content(9000):
                    download_file.write(chunk)


if __name__ == '__main__':
    main()
