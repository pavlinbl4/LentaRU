import requests
import json
from tools.create_subfolder import create_directory
from tools.get_file_name import ImageNamer

from tools.get_html import get_html


def main():
    for day_shift in range(2):

        autor = "Фото: Евгений Павленко / «Коммерсантъ»"

        url = f"https://lenta.ru/search/v2/process?from={str(day_shift)}" \
              f"&size=10&sort=2&title_only=0&domain=1&modified,format=yyyy-MM-dd&query={autor}"
        rezult = json.loads(get_html(url))

        path_to_folder = create_directory("Kommersant/LentaRU/Евгений Павленко")

        for i in rezult['matches']:
            print(i['image_url'])
            filename = f"{ImageNamer().file_name(i['image_url'])}.JPG"
            r = requests.get(i['image_url'])
            with open(f'{path_to_folder}/{filename}', 'wb') as download_file:
                for chunk in r.iter_content(9000):
                    download_file.write(chunk)


if __name__ == '__main__':
    main()
