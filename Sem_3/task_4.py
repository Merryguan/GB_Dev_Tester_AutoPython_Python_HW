# Семинар 3

# Задание №4. Генерация паролей

# Условие:
# Напишите программу, которая генерирует случайный пароль заданной длины,
# состоящий из букв, цифр и специальных символов.

# Решение:
import string
import  random

length = 10

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for i in range(length))

print(password)
