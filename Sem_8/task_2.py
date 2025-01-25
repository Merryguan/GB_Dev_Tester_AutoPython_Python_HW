# Семинар 8. Сериализация.

# Задание №2. Объединение данных из нескольких JSON файлов.

# Условие:
# Напишите скрипт,
# который объединяет данные из нескольких JSON файлов в один.
# Каждый файл содержит список словарей,
# описывающих сотрудников компании (имя, фамилия, возраст, должность).
# Итоговый JSON файл должен содержать объединённые списки сотрудников из всех файлов.
# Пример: У вас есть три файла employees1.json, employees2.json,
# employees3.json. Нужно объединить их в один файл all_employees.json.

# Решение:
import json
from pathlib import Path
import glob

_PATH_1 = Path.cwd() / "input" / "Zad_2" / "*.json"
_PATH_2 = Path.cwd() / "input" / "Zad_2" / "all_employees.json"

result = list()


def merge_json_files(input_files: str, ouput_file: str):
    merged_data = list()
    for file in input_files:
        try:
            with open(file, 'r') as input_file:
                raw_json = json.load(input_file)
                merged_data.extend(raw_json)
        except json.JSONDecodeError:
            print(f"Ошибка чтения JSON файла {file}")
    with open(ouput_file, 'w') as output_file:
        json.dump(merged_data, output_file, indent=4)


if __name__ == "__main__":
    json_files = glob.glob(str(_PATH_1))
    merge_json_files(json_files, str(_PATH_2))

