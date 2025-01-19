# Семинар 6. Модули

# Задание №1. Модуль для подсчета количества повторений слов.

# Условие:
# Создайте модуль с функцией,
# которая получает список слов и
# возвращает словарь,
# в котором ключи — это слова,
# а значения — количество их повторений в списке.

# Решение:
def repeat_word_count(word_list):
    result_dict = dict()
    for item in word_list:
        result_dict[item] = result_dict.get(item, 0) + 1
    return result_dict


input_list = ["apple", "banana", "apple", "orange"]
print(repeat_word_count(input_list))
