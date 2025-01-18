# Семинар 4

# Задание №1. Апгрейд калькулятора

# Условие:
# Степан использует калькулятор для расчёта суммы и разности чисел, но на
# работе ему требуются не только обычные арифметические действия. Он ничего
# не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.
# Напишите программу,
# запрашивающую у пользователя число и действие,
# которое нужно сделать с числом:
# вывести сумму его цифр,
# максимальную или минимальную цифру.
# Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и
# минимума при помощи аргументов.

# Решение:
def sum_of_digits(num):
    result = 0
    while num > 0:
        result = result + num % 10
        num = num // 10
    print(result)


def max_digit(num):
    result = num % 10
    while num > 0:
        if num % 10 > result:
            result = num % 10
        num = num // 10
    print(result)


def min_digit(num):
    result = num % 10
    while num > 0:
        if num % 10 < result:
            result = num % 10
        num = num // 10
    print(result)


while True:
    number = int(input("Введите число: "))
    choice = input("Введите действие(q, s, m, l: ")
    if choice == 'q':
        break
    elif choice == 's':
        sum_of_digits(number)
    elif choice == 'm':
        max_digit(number)
    elif choice == 'l':
        min_digit(number)
