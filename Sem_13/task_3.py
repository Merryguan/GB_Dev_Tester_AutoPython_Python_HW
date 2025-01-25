"""
 Семинар 13. Исключения.

 Задание №3. Счастливое число.

 Условие:
 Напишите программу,
 которая запрашивает у пользователя число до тех пор,
 пока сумма этих чисел не станет больше либо равна 777.
 Каждое введенное число при этом дозаписывается в файл.
 Сделайте так,
 чтобы перед дозаписью
 программа с вероятностью 1 к 13 выбрасывала пользователю случайное исключение
 и завершалась.
 Пример 1:
 Введите число: 10
 Введите число: 500
 Введите число: 200
 Введите число: 67
 Вы успешно выполнили условие для выхода из порочного цикла!
 Содержимое файла out_file.txt:
 10
 500
 200
 67
 Пример 2:
 Введите число: 10
 Введите число: 500
 Вас постигла неудача!
 Содержимое файла out_file.txt:
 10
"""

# Решение:
from os import remove
from pathlib import Path
from random import randint

_PATH = Path.cwd() / "output" / "task_3" / "out_file.txt"


class MagicFileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        #self.file_path = self.get_file_path()
        self.magic_sum = 0

    @staticmethod
    def is_exception_raise():
        return randint(1, 13) == 1

    def pre_init(self):
        try:
            remove(self.file_path)
        except OSError as ex:
            print(ex)
            print('Данный файл не может быть удален')

    def process_input(self):
        try:
            input_number = int(input('Введите число: '))
            self.magic_sum = self.magic_sum + input_number
            if self.is_exception_raise():
                raise Exception('Вас постигла неудача!')
            with open(self.file_path, 'a') as out_fd:
                out_fd.write(str(input_number) + '\n')
        except (ValueError, KeyboardInterrupt) as ex:
            print(ex)
            print('Возникли проблемы при вводе.')
            print('Попробуйте еще раз')

    def run(self):
        self.pre_init()
        while self.magic_sum < 777:
            self.process_input()
        print('Вы успешно выполнили условие для выхода из порочного цикла!')



class FailException(Exception):
    def __init__(self):
        super().__init__("Вас постигла неудача!")


if __name__ == "__main__":
    processor = MagicFileProcessor(str(_PATH))
    processor.run()