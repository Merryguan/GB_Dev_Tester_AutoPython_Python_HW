# Семинар 4

# Задание №4. Функция максимума

# Условие:
# Юра пишет различные полезные функции для Python, чтобы остальным
# программистам стало проще работать. Он захотел написать функцию, которая
# будет находить максимум из перечисленных чисел. Функция для нахождения
# максимума из двух чисел у него уже есть. Юра задумался: может быть, её
# можно как-то использовать для нахождения максимума уже от трёх чисел?
# Помогите Юре написать программу, которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.
# По итогу в программе должны быть реализованы две функции:
# 1. maximum_of_two — функция принимает два числа и возвращает одно
# (наибольшее из двух);
# 2. maximum_of_three — функция принимает три числа и возвращает одно
# (наибольшее из трёх); при этом она должна использовать для сравнений
# первую функцию maximum_of_two.

# Решение:
def maximum_of_two(number1, number2):
    return number1 if number1 > number2 else number2


def maximum_of_three(number1, number2, number3):
    return maximum_of_two(number1, maximum_of_two(number2, number3))

print("Самое большое число:", maximum_of_three(150, 65, 105))