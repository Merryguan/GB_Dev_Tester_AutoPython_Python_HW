# Семинар 7. Файлы и файловая система.
import zipfile
# Задание №2. Создание архива каталога.

# Условие:
# Напишите скрипт, который создает архив каталога в формате .zip.
# Скрипт должен принимать путь к исходному каталогу
# и путь к целевому архиву.
# Архив должен включать все файлы и подпапки исходного каталога.

# Решение:
from os import path, listdir, walk
from zipfile import ZipFile


def backup_files(input_directory_str: str, output_directory_str: str):
    #files = list()
    if path.isdir(input_directory_str):
        #files = walk(input_directory_str)
        with ZipFile(output_directory_str, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in walk(input_directory_str):
                for file in files:
                    file_path = path.join(root, file)
                    zipf.write(file_path, path.relpath(file_path, input_directory_str))
    else:
        raise FileNotFoundError(f"Каталог {input_directory_str} не найден.")
    pass

input_path_str = "E:\Homework\GB_Dev_Tester_AutoPython_Python_HW\Sem_7\in"
output_path_str = "E:\Homework\GB_Dev_Tester_AutoPython_Python_HW\Sem_7\out\\backup.zip"
backup_files(input_path_str, output_path_str)
