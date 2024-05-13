import json
import time

from tools.get_html import get_html


def main():
    for i in range(0, 51, 10):

        autor = 'Евгений Павленко'

        url = (f'https://lenta.ru/search/v2/process?from={i}'
               f'&size=10&sort=2&title_only=0&domain=1&modified,format=yyyy-MM-dd&query='
               f'Фото: {autor} / «Коммерсантъ»')

        rezult = json.loads(get_html(url))
        print(f"page number: {i}, записи в файле {len(rezult['matches'])}")
        print()

        for i in rezult['matches']:
            main_data = {'title': i['title'], 'image_url': i['image_url'], 'url': i['url'],
                         'pubdate': time.ctime(i['pubdate'])}
            print(main_data['pubdate'], '-', main_data['title'] + '\n' + main_data['image_url'] + '\n')


if __name__ == '__main__':
    main()
