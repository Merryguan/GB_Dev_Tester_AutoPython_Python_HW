# Семинар 8. Сериализация.

# Задание №3. Агрегирование данных из CSV файла.

# Условие:
# Напишите скрипт,
# который считывает данные из JSON файла
# и сохраняет их в CSV файл.
# JSON файл содержит данные о продуктах
# (название, цена, количество на складе).
# В CSV файле каждая строка должна соответствовать одному продукту.

# Решение:
import json
import csv
from pathlib import Path

_PATH_1 = Path.cwd() / "input" / "Zad_3" / "products.json"
_PATH_2 = Path.cwd() / "input" / "Zad_3" / "products.csv"


def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as input_file:
        raw_json = json.load(input_file)
    if not isinstance(raw_json, list) or not all(isinstance(item, dict) for item in raw_json):
        raise ValueError("Некорректный формат данных в JSON файле")
    with open(csv_file, 'w', newline='') as output_file:
        fieldsnames = raw_json[0].keys()
        writer = csv.DictWriter(output_file, fieldnames=fieldsnames)
        writer.writeheader()
        writer.writerows(raw_json)


if __name__ == "__main__":
    json_to_csv(_PATH_1, _PATH_2)
