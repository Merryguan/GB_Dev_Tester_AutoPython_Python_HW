# Семинар 2

# Задание №3. Перевод целого числа в римское число

# Условие:
# Программа принимает целое число и возвращает его римское представление в
# виде строки.

# Решение:
# M = 1000 mille
# D - 500 quingenti
# C - 100 centum
# L - 50 quinqu
# X - 10 decem
# V - 5 quinque
# I - 1 unus
val = [1000, 900, 500, 400,
       100, 90, 50, 40,
       10, 9, 5, 4,
       1]

syb = ["M", "CM", "D", "CD",
       "C", "XC", "L", "XL",
       "X", "IX", "V", "IV",
       "I"]

arabian_num = 2613
roman_num = ""

i = 0

while arabian_num > 0:
    for _ in range(arabian_num // val[i]):
        roman_num = roman_num + syb[i]
        arabian_num = arabian_num - val[i]
    i = i + 1


print(roman_num)
