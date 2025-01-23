# Семинар 8. Сериализация.

# Задание №4. Агрегирование данных из CSV файла.

# Условие:
# Напишите скрипт,
# который считывает данные из CSV файла,
# содержащего информацию о продажах (название продукта, количество, цена за единицу),
# и подсчитывает общую выручку для каждого продукта.
# Итог должен быть сохранён в новом CSV файле.
# Пример: Из файла sales.csv нужно создать файл total_sales.csv, где для каждого
# продукта будет указана общая выручка.

# Решение:
import csv
from pathlib import Path

_PATH_1 = Path.cwd() / "sources" / "Zad_4" / "sales.csv"
_PATH_2 = Path.cwd() / "sources" / "Zad_4" / "total_sales.csv"


def calculate_total_sales(input_csv, output_csv):
    sales_totals = dict()
    with open(input_csv, 'r') as input_file, \
            open(output_csv, 'w', newline='') as output_file:
        raw_csv = csv.DictReader(input_file)
        for good in raw_csv:
            product = good["product"]
            quantity = int(good["quantity"])
            price_per_unit = float(good["price"])
            total_sales = round(quantity * price_per_unit, ndigits=2)
            if product in sales_totals:
                sales_totals[product] = sales_totals[product] + total_sales
            else:
                sales_totals[product] = total_sales
        fieldnames = ["product", "total price"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        for product, total_sales in sales_totals.items():
            writer.writerow({'product': product, 'total price': total_sales})


if __name__ == "__main__":
    calculate_total_sales(_PATH_1, _PATH_2)
