# Семинар 7. Файлы и файловая система.

# Задание №1. Функция группового переименования файлов.

# Условие:
# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов.
#   При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла.
#   Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
#   Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#   К ним прибавляется желаемое конечное имя, если оно передано.
#   Далее счётчик файлов и расширение.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет
# для работы с файлами.

# Решение:
from os import listdir, path, chdir


def mass_rename(directory, num_digits: int,
                input_file_extension_str: str, output_file_extension_str: str,
                name_range_lst: list,
                file_name_str = ''):
    files_lst = [file for file in listdir(directory) if file.endswith(input_file_extension_str)]
    if not files_lst:
        print("Файлы с указанным расширением не найдены.")
        return
    new_file_name_str = ''
    if path.isdir(directory):
        for index, file in enumerate(files_lst, start=1):
            start, stop = name_range_lst
            new_file_name_str = f"{file[start - 1:stop]}{file_name_str}{index:0{num_digits}d}.{output_file_extension_str}"
            out_path_str = "E:\Homework\GB_Dev_Tester_AutoPython_Python_HW\Sem_7\out"
            chdir(out_path_str)
            open(new_file_name_str, 'a').close()
    else:
        raise FileNotFoundError(f"Каталог {directory} не найден.")


path_str = "E:\Homework\GB_Dev_Tester_AutoPython_Python_HW\Sem_7\in"
mass_rename(path_str, 3, "txt", "docx", [1, 3], "hex")

'''
if __name__ == "__main__":
import sys
# Проверяем количество аргументов командной строки
if len(sys.argv) != 6:
print("Usage: python file_rename.py <directory> <final_name>
<num_digits> <old_extension> <new_extension>")
sys.exit(1)
directory = sys.argv[1]
final_name = sys.argv[2]
num_digits = int(sys.argv[3])
old_extension = sys.argv[4]
new_extension = sys.argv[5]
# Например, диапазон [3, 6]
name_range = [3, 6]
'''
