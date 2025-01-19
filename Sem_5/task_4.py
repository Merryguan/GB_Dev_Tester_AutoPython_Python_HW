# Семинар 5

# Задание №4. Генератор подстрок.

# Условие:
# Напишите генераторную функцию substrings(s),
# - которая принимает строку s и
# - возвращает генератор всех возможных подстрок этой строки.
# Пример:
# На вход подается строка abc
# На выходе будут выведены обозначения:
# a
# ab
# abc
# b
# bc
# c

# Решение:
def substrings(s):
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield s[start:end]


for item in substrings("abc"):
    print(item)
