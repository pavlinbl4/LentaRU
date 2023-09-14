import csv


def csv_writer(i):
    with open("lenta_ru.csv", 'a') as input_file:
        columns = ['title', 'image_url', 'url', "pubdate"]
        writer = csv.DictWriter(input_file, fieldnames=columns)
        writer.writerow(i)
