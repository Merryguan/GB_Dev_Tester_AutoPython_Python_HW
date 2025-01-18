# Семинар 3

# Задание №1. Удаление дубликатов из списка

# Условие:
# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.

# Решение:
my_list = [1, 4, 5, 1, 7, 4, 7, 4, 9]

dup_list = list()

for elem in my_list:
    if my_list.count(elem) > 1 and elem not in dup_list:
        dup_list.append(elem)

print(my_list)
print(dup_list)
