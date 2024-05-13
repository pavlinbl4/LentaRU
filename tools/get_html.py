from fake_headers import Headers
import requests
import time


def get_html(url):
    headers = Headers().generate()
    time.sleep(1)
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        time.sleep(10)
        print("bad status code")
        r = requests.get(url, headers=headers)
    return r.text


class WebScraper:
    def __init__(self):
        self.headers = Headers().generate()

    def get_html(self, url):
        time.sleep(1)
        r = requests.get(url, headers=self.headers)
        if r.status_code != 200:
            time.sleep(10)
            print("Bad status code, retrying...")
            r = requests.get(url, headers=self.headers)
        return r.text


if __name__ == '__main__':

    scraper = WebScraper()
    html = scraper.get_html("http://example.com")
    print(html)