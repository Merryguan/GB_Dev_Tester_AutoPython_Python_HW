# Семинар 2

# Задание №2. Преобразование числа в шестнадцатеричное
# представление

# Условие:
# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для
# проверки своего результата.

# Решение:
num = 490
hex_digits = "0123456789ABCDEF"


def dec_to_hex(number):
    result = ""

    if number < 0:
        result = result + "-"
        number = abs(number)

    if number == 0:
        result = 0

    while number > 0:
        result = result + hex_digits[number % 16]
        number = number // 16

    return result


print(dec_to_hex(num))
print(hex(num))