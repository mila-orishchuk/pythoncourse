"""
notifier = notify(every=1000)
создали нотификатор и внутри цикла дергаем его а он каждые 1000 раз
выводит "Итерация __ выполнена" 
(используется при генерации допустим большого файла чтоб видеть на какой стадии процесс)
"""


def notify(dataset=range(10000), every=1000):
    for i in dataset:
        if not i % every:
            yield "Итерация __ выполнена"


if __name__ == '__main__':
    notifier = notify(every=1000)
    for i in notifier:
        print(i)
