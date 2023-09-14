import re
def file_name(image_url):
    pattern = r'2023\d+'
    return re.search(pattern, image_url).group()


if __name__ == '__main__':
    print(file_name('icdn.lenta.ru/images/2023/09/07/12/20230907122611781/detail_03a36d0dca24fdef2b3d56c2ca27d587.jpg'))
