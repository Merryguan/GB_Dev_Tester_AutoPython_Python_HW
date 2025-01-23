# Семинар 8. Сериализация.

# Задание №1. Работа с основными данными.

# Условие:
# Напишите функцию,
# которая получает на вход директорию
# и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и
# pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке
# и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

# Решение:
from pathlib import Path
from os import walk
from os import path
import json
import csv
import pickle

_PATH = Path.cwd() / "Sources"


def get_size(dir_path: str):
    if path.isfile(dir_path):
        return path.getsize(dir_path)
    elif path.isdir(dir_path):
        total_size = 0
        for root_name, _, filenames in walk(dir_path):
            for filename in filenames:
                file_path = path.join(root_name, filename)
                total_size += path.getsize(file_path)
        return total_size


def get_info(base_dir: str = _PATH):
    files = list()
    for root_name, dirs_name, filenames in walk(_PATH):
        for name in dirs_name + filenames:
            file_path = path.join(root_name, name)
            file = {"name": name,
                    "path": file_path,
                    "type": "Directory" if path.isdir(file_path) else "File",
                    "size": get_size(file_path),
                    "parent": path.basename(root_name)}
            files.append(file)
    return files


def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['name', 'path', 'type', 'size', 'parent'])
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle(data, filename):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


def main(directory):
    data = get_info(directory)
    save_to_json(data, 'directory_info.json')
    save_to_csv(data, 'directory_info.csv')
    save_to_pickle(data, 'directory_info.pkl')


if __name__ == "__main__":
    main(_PATH)