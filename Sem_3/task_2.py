# Семинар 3

# Задание №2. Поиск наибольшего числа в списке

# Условие:
# Напишите программу, которая принимает список чисел через строку и
# возвращает наибольшее число в этом списке.

# Решение:
input_str = "1, 4, 5, 1, 7, 4, 7, 4, 9"
max_digital = 0

for elem in input_str.split():
    if elem.isdigit() > max_digital:
        max_digital = elem

print(input_str)
print(max_digital)
