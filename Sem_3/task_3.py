# Семинар 3

# Задание №3. Проверка палиндрома

# Условие:
# Напишите программу, которая принимает строку и определяет, является ли она
# палиндромом (читается одинаково с обеих сторон).

# Решение:
input_str = "а роза упала на лапу азора".lower().replace(' ','')

odd_chars = set()

for elem in input_str:
    if elem in odd_chars:
        odd_chars.remove(elem)
    else:
        odd_chars.add(elem)

if len(odd_chars) <= 1:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
