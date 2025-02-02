# Семинар 5

# Задание №1. Квадраты чисел.

# Условие:
# Пользователь вводит число N.
# Напишите программу, которая генерирует последовательность
# из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее).
# Реализацию напишите двумя способами: функция-генератор и генераторное выражение.

# Решение:
n = 10


def pow_gen(number):
    for count in range(1, number + 1):
        yield count ** 2


result = (item ** 2 for item in range(1, n + 1))
