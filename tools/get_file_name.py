import datetime
import re
from datetime import date


class ImageNamer:
    def __init__(self):
        today_year = str(date.today().strftime('%Y'))
        self.pattern = rf'{today_year}\d+'

    def file_name(self, image_url):
        match = re.search(self.pattern, image_url)
        if match:
            return match.group()
        else:
            return None


if __name__ == '__main__':
    example_image_url = 'http://example.com/image_2024145.jpg'
    print(ImageNamer().file_name(example_image_url))
