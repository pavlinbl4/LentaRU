import re



def data_from_link(lentaru_url):
    pattern = r'(?<=\/)\d{17}'
    return re.search(pattern, lentaru_url).group()

if __name__ == '__main__':
    print(data_from_link('https://icdn.lenta.ru/images/2023/11/17/10/20231117103028298/detail_a4e58498a75407f2c3b19350f0c97af1.jpg'))
