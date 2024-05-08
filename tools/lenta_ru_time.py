from datetime import datetime
import time


def lenta_ru_time_converter(lenta_ru_time):
    return datetime.strptime(time.ctime(lenta_ru_time), '%a %b %d %H:%M:%S %Y').strftime('%Y-%m-%d')