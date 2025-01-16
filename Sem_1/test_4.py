# Семинар 1

# Задание №4. Яма

# Условие:
# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
# Вам поручили создать генератор ландшафта. Напишите программу, которая
# получает на вход число N и выводит на экран числа в виде ямы

# Решение:
depth = 5
point = "."
left = ""
right = ""

for line in range(depth):
    for left in range(0, line + 1):
        print(depth - left, end="")
    print(2 * (depth - line - 1) * point, end="")
    for right in range(depth - line, depth + 1):
        print(right, end="")
    print()