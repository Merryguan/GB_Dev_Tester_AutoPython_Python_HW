"""
 Семинар 13. Исключения.

 Задание №1. Карма.

 Условие:
 Один буддист-программист решил создать свой симулятор жизни,
 в котором нужно набрать 500 очков кармы (это константа),
 чтобы достичь просветления.
 Каждый день вызывается специальная функция one_day(),
 которая возвращает количество кармы от 1 до 7
 и может с вероятностью 1 к 10 выкинуть одно из исключений:
 - KillError,
 - DrunkError,
 - CarCrashError,
 - GluttonyError,
 - DepressionError.
 (Исключения нужно создать самостоятельно, при помощи наследования от Exception.)
 Напишите такую программу.
 Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении кармы до уровня константы.
 Исключения обработайте и запишите в отдельный лог karma.log.
 По итогу у вас может быть примерно такая структура программы:
 открываем файл
 цикл по набору кармы
 try
 карма += one_day()
 except(ы) с указанием классов исключений, которые нужно поймать
 добавляем запись в файл
 закрываем файл
"""

# Решение:
from pathlib import Path
from random import randint

_PATH = Path.cwd() / "output" / "task_1" / "karma.log"


class KillError(Exception):
    def __init__(self):
        super().__init__("Убийство. Вы и убили-с!")


class DrunkError(Exception):
    def __init__(self):
        super().__init__("Пьянство. Пьянству бой!")


class CarCrashError(Exception):
    def __init__(self):
        super().__init__("Вы попали в аварию. Стоит следить за дорогой.")


class GluttonyError(Exception):
    def __init__(self):
        super().__init__("Вы обожрались. Следует сократить порции.")


class DepressionError(Exception):
    def __init__(self):
        super().__init__("На вас напала хандра. Уныние - грех.")


def one_day():
    if randint(1, 10) == 1:
        exceptions_list = [KillError,
                           DrunkError,
                           CarCrashError,
                           GluttonyError,
                           DepressionError]
        raise exceptions_list[randint(0, 4)]
    return randint(1, 7)


def main():
    nirvana = 500
    karma = 0
    with open(str(_PATH), 'w', encoding="utf-8") as log:
        while karma < nirvana:
            try:
                karma = karma + one_day()
            except Exception as ex:
                log.write(f"{ex}\n")


print('Вы достигли Нирваны! ')
print('Омм ')


if __name__ == "__main__":
    main()
