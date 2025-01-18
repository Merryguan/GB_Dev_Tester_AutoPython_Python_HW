# Семинар 4

# Задание №3. Число наоборот

# Условие:
# Пользователь вводит два числа: N и K. Напишите программу, которая заменяет
# каждое число на число, которое получается из исходного записью его цифр в
# обратном порядке, затем складывает их, снова переворачивает и выводит
# ответ на экран.

# Решение:
def reverse_number(number):
    result = ''
    count = 0
    while number > 0:
        result = result + f"{number % 10}"
        number = number // 10
        count = count + 1
    return int(result)


num1 = 405
print(f"Заданне число: {num1}")
num1 = reverse_number(num1)
print(f"Перевернутое число: {num1}")
num2 = 570
print(f"Заданне число: {num2}")
num2 = reverse_number(num2)
print(f"Перевернутое число: {num2}")
my_sum = num1 + num2
print(f"Сумма: {my_sum}")
my_sum = reverse_number(my_sum)
print(f"Перевернутое число: {my_sum}")