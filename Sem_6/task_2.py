# Семинар 6. Модули

# Задание №2. Модуль для удаления дублирующихся подряд символов.

# Условие:
# Напишите модуль с функцией,
# которая принимает строку и
# возвращает строку с удаленными дублирующимися подряд идущими символами.
# Например,
# строка "aabbccaa" должна быть преобразована в "abca".

# Решение:
def remove_char_duplicates(input_str: str):
    result_str = ''
    j = 0
    if not input_str:
        return input_str
    char_list = list(input_str[0])
    for item in input_str[1:]:
        if item != char_list[-1]:
            char_list.append(item)
    return result_str.join(char_list)


my_str = "aabbccaa"
print(remove_char_duplicates(my_str))
