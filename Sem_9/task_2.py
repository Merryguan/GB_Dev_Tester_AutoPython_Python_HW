# Семинар 9. Декораторы.

# Задание №2. Замедление кода.

# Условие:
# В программировании иногда возникает ситуация,
# когда работу функции нужно замедлить.
# Типичный пример —
# функция, которая постоянно проверяет,
# изменились ли данные на веб-странице или её код.
# Реализуйте декоратор,
# который перед выполнением декорируемой функции ждёт несколько секунд.

# Решение:
from functools import wraps
from time import sleep
from typing import Callable


def freezing(func: Callable) -> Callable:
    @wraps(func)
    def wrapper():
        sleep(5)
        return func()
    return wrapper


@freezing
def test():
    print("<Тут что-то произходит...>")


if __name__ == "__main__":
    test()