import fake_headers
import requests
import time


def get_html(url):
    headers = fake_headers.Headers().generate()
    time.sleep(1)
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        time.sleep(10)
        print("bad status code")
        r = requests.get(url, headers=headers)
    return r.text