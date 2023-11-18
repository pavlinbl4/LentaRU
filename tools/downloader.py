import requests


def image_downloader(image_url: str, path_to_folder: str, filename: str):
    with open(f'{path_to_folder}/{filename}', 'wb') as download_file:
        response = requests.get(image_url)
        for chunk in response.iter_content(9000):
            download_file.write(chunk)
    return f'{path_to_folder}/{filename}'
