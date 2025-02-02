# Семинар 9. Декораторы.

# Задание №1. Как дела?

# Условие:
# Вася совсем заскучал на работе и решил побаловаться с кодом проекта.
# Он написал надоедливый декоратор,
# который при вызове декорируемой функции спрашивает у пользователя «Как дела?»,
# вне зависимости от ответа пишет что-то вроде «А у меня не очень!»
# и только потом запускает саму функцию.
# Правда, после такой выходки Васю чуть не уволили с работы.
# Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.
# Пример кода:
# @how_are_you
# def test():
# print('<Тут что-то происходит...>')
# test()
# Результат:
# Как дела? Хорошо.
# А у меня не очень! Ладно, держи свою функцию.
# <Тут что-то происходит...>

# Решение:
from functools import wraps
from typing import Callable
def how_are_you(func: Callable) -> Callable:
    @wraps(func)
    def wrapper():
        input("Как дела? ")
        print("А у меня не очень!")
        result = func()
        return result
    return wrapper


@how_are_you
def test():
    print("<Тут что-то произходит...>")


if __name__ == "__main__":
    test()