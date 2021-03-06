from faker import Faker
fake = Faker()
import random
import json

def main(): #Генерирует список из 100 случайно сгенерированных книг и записывает в файл в формате JSON.
   list_books = {}
   for i in range(1, 101):
       list_books[i] = {"Год": year(),
                        "Страниц": pages(),
                        "Идентификатор isbn13": isbn13(),
                        "Рейтинг": rating(),
                        "Цена": price(),
                        "Автор": author(),
                        "Заголовок": title()}
       with open("Book", 'w', encoding='utf-8') as f:
           json.dump(list_books, f, indent=4, ensure_ascii=False)



def title():
    """
    заголовок из файла
    :return:
    """
    filename = "books.txt"
    with open(filename, encoding="utf-8") as f:
        title_lines = f.readlines()
        return random.choice(title_lines)

def year():
    """
    генерация года книги от 1900 до 1980 года
    :return:
    """
    year_ = random.randint(1900, 1980)
    return year_

def pages():
    """
    генерация страниц книги от 100 до 250 страниц
    :return:
    """
    pages_ = random.randint(100, 250)
    return pages_

def isbn13():
    """
    генерация номера книги isbn13
    :return:
    """
    isbn13_ = fake.isbn13()
    return isbn13_


def rating() -> float:
    """
    генерация рейтинга книги с плавающей запятой
    :return:
    """
    rating_ = round(random.uniform(1, 5), 1)
    return rating_

def price():
    """
     #генерация цены книги
    :return:
    """
    price_ = round(random.uniform(150, 300), 2)
    return price_

def author():
    """
    генерация автора книги
    :return:
    """
    fake = Faker('ru_RU')
    author_ = fake.name()
    return author_

if __name__ == "__main__":
    main()
