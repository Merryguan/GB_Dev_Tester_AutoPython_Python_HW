# Семинар 4

# Задание №4. Яйца

# Условие:
# В рамках программы колонизации Марса компания «Спейс Инжиниринг»
# вывела особую породу черепах, которые, по задумке, должны размножаться,
# откладывая яйца в марсианском грунте. Откладывать яйца слишком близко к
# поверхности опасно из-за радиации, а слишком глубоко — из-за давления
# грунта и недостатка кислорода. Вообще, факторов очень много, но
# специалисты проделали большую работу и предположили, что уровень
# опасности для черепашьих яиц рассчитывается по формуле: D = x^3 − 3x^2 −
# 12x + 10, где x — глубина кладки в метрах, а D — уровень опасности в
# условных единицах. Для тестирования гипотезы нужно взять пробу грунта на
# безопасной, согласно формуле, глубине.
# Напишите программу, находящую такое значение глубины х, при котором
# уровень опасности как можно более близок к нулю. На вход программе
# подаётся максимально допустимое отклонение уровня опасности от нуля, а
# программа должна рассчитать приблизительное значение х, удовлетворяющее
# этому отклонению. Известно, что глубина точно больше нуля и меньше четырёх
# метров. Обеспечьте контроль ввода.
# Пример:
# Введите максимально допустимый уровень опасности: 0.01
# Приблизительная глубина безопасной кладки: 0.732421875 м

# Решение:
def calculate_danger(depth):
    return depth ** 3 - 3 * depth ** 2 - 12 * depth + 10


def find_safe_depth(max_danger):
    max_depth = 4
    while True:
        danger = calculate_danger(0.7324)
        print(danger)
        if abs(danger) < max_danger:
            print(f"Глубина безопасной кладки: {max_depth} метра")
            break
        max_depth = max_depth / 2
        #print(max_depth)
        if max_depth == 0:
            break


find_safe_depth(0.01)
