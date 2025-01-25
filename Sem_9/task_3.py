# Семинар 9. Декораторы.

# Задание №3. Счётчик.

# Условие:
# Реализуйте декоратор counter,
# считающий и выводящий количество вызовов декорируемой функции.
# Для решения задачи нельзя использовать операторы global и nonlocal.
# Пример: Из файла products.json нужно создать products.csv.

# Решение:
from functools import wraps
from typing import Callable
def count_calls(func: Callable) -> Callable:
    @wraps(func)
    def wrapper():
        wrapper.count = wrapper.count + 1
        result = func()
        print(f"Функцию {func.__name__} вызвали {wrapper.count} раз")
        return result
    wrapper.count = 0
    return wrapper


@count_calls
def test():
    print("<Тут что-то произходит...>")


if __name__ == "__main__":
    test()