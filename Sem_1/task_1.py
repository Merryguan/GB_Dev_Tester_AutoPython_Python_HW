# Семинар 1

# Задание №1. Рамка

# Условие:
# Напишите программу,
# которая рисует прямоугольную рамку с помощью символьной графики.
# Для вертикальных линий используйте символ вертикального штриха (|),
# а для горизонтальных — дефис (-).
# Пусть ширину и высоту рамки определяет пользователь.

# Решение:
horizontal = "-"
vertical = "|"
space = " "
result = ""
height = 17
wight = 6

result = vertical + height * horizontal + vertical
print(result)
for i in range(0, wight):
    result = vertical + height * space + vertical
    print(result)
result = vertical + height * horizontal + vertical
print(result)