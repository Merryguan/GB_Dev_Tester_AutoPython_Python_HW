# Семинар 8. Сериализация.

# Задание №5. Конвертация CSV в JSON с изменением структуры данных.

# Условие:
# Напишите скрипт,
# который считывает данные из CSV файла
# и сохраняет их в JSON файл с другой структурой.
# CSV файл содержит данные о книгах (название, автор, год издания).
# В JSON файле данные должны быть сгруппированы по авторам,
# а книги каждого автора должны быть записаны как список.
# Пример: Из файла books.csv нужно создать файл books_by_author.json, где
# книги сгруппированы по авторам.

# Решение:
import csv
import json
from pathlib import Path

_PATH_1 = Path.cwd() / "input" / "Zad_5" / "books.csv"
_PATH_2 = Path.cwd() / "input" / "Zad_5" / "books_by_author.json"


def convert_csv_to_json(input_csv, output_json):
    books_by_author = {}
    with (open(input_csv, 'r') as input_file,
          open(output_json, 'w') as output_file):
        raw_csv = csv.DictReader(input_file)
        for row in raw_csv:
            author = row['автор']
            book = {
                'название': row['название'],
                'год издания': row['год издания']
            }
            if author in books_by_author:
                books_by_author[author].append(book)
            else:
                books_by_author[author] = [book]
        json.dump(books_by_author, output_file, indent=4)


if __name__ == "__main__":
    convert_csv_to_json(_PATH_1, _PATH_2)