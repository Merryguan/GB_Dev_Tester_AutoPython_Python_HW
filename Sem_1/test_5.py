# Семинар 1

# Задание №5. Яма

# Условие:
# Мальчик загадывает число между 1 и 100 (включительно). Компьютер может
# спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер. Мальчик отвечает одним из
# трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
# Напишите программу, которая с помощью цепочки таких вопросов и ответов
# мальчика угадывает число.
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать
# число за семь попыток.

# Решение:
from random import randint
start = 1
finish = 100
count = 0
answer = randint(start, finish)
number = (finish - start) // 2
question = number

while True:
    count = count + 1
    print(f"Твоё число равно, меньше или больше, чем число {question}?")
    #answer = int(input())
    number = 1 if number < 1 else number // 2
    if answer == question:
        print(f"Загаданное число равно {question}")
        break
    elif question < answer:
        question = question + number
    elif answer < question:
        question = question - number
print(count)
