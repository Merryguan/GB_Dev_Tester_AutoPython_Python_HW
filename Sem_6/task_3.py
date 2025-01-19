# Семинар 6. Модули

# Задание №3. Модуль для нахождения уникальных для обоих списков
# элементов.

# Условие:
# Создайте модуль с функцией,
# которая принимает два списка
# и возвращает список,
# содержащий только элементы, которые уникальны для обоих списков.

# Решение:
def find_unique_elements(input_list_1: list, input_list_2: list):
    transit_set_1 = set(input_list_1)
    transit_set_2 = set(input_list_2)
    result_set = (transit_set_1 - transit_set_2).union(transit_set_2 - transit_set_1)
    return list(result_set)


my_list_1 = [1, 2, 3]
my_list_2 = [3, 4, 5]
print(find_unique_elements(my_list_1, my_list_2))
