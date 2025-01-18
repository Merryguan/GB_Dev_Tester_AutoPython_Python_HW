# Семинар 4

# Задание №2. Недоделка

# Условие:
# Вы пришли на работу в компанию по разработке игр, целевая аудитория —
# дети и их родители. У предыдущего программиста было задание сделать две
# игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# Однако программист, на место которого вы пришли, перед увольнением не
# успел выполнить эту задачу и оставил только небольшой шаблон проекта.
# Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай
# число».
# Правила игры «Камень, ножницы, бумага»: программа запрашивает у
# пользователя строку и выводит, победил он или проиграл. Камень бьёт
# ножницы, ножницы режут бумагу, бумага кроет камень.
# Правила игры «Угадай число»: программа запрашивает у пользователя число
# до тех пор, пока он не отгадает загаданное.

# Решение:
def rock_paper_scissors():
    choice_list = ["камень", "ножницы", "бумага"]
    choice_user = choice_list[int(input("Введите 1 - камень, 2 - ножницы или 3 - бумага: ")) - 1]
    if choice_user not in choice_list:
        return "Неверный ввод"
    choice_comp = choice_list[1]
    if choice_user == choice_list[0] and choice_comp == choice_list[1]:
        print("Вы победили")
    elif choice_user == choice_list[1] and choice_comp == choice_list[2]:
        print("Вы победили")
    elif choice_user == choice_list[2] and choice_comp == choice_list[0]:
        print("Вы победили")
    elif choice_user == choice_comp:
        print("Ничья")
    else:
        print("Вы проиграли")


def guess_the_number():
    while True:
        choice_comp = 304
        choice_user = int(input("Введите число: "))
        if choice_user > choice_comp:
            print("Число больше загаданного")
        elif choice_user < choice_comp:
            print("Число меньше загаданного")
        if choice_user == choice_comp:
            print("Вы угадали")
            break


def mainMenu():
    while True:
        choice_user = int(input("Введите 1 - «Камень, ножницы, бумага», 2 - «Угадай число», 3 - выход: "))
        if choice_user == 1:
            rock_paper_scissors()
        elif choice_user == 2:
            guess_the_number()
        elif choice_user == 3:
            break
        else:
            print("Невнрная команда")


mainMenu()
