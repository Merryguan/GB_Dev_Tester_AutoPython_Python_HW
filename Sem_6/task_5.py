# Семинар 6. Модули

# Задание №5. Модуль для проверки ферзей.

# Условие:
# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него
# напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно
# расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
# ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 -
# координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют
# - ложь.

# Решение:
def are_queens_safe(positions):
    def is_under_attack(row, col):
        for i in range(8):
            if i != row:
                if (positions[i][1] == col or
                        abs(positions[i][0] - row) ==
                        abs(positions[i][1] - col)):
                    return True
        return False

    for i in range(8):
        if is_under_attack(positions[i][0], positions[i][1]):
            return False
    return True


def generate_random_queens_placement():
    import random
    return [(i, random.randint(1, 8)) for i in range(8)]


def print_valid_placements(num_placements=4):
    count = 0
    while count < num_placements:
        placement = generate_random_queens_placement()
        if are_queens_safe(placement):
            print(placement)
            count += 1


print_valid_placements(8)
