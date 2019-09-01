# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import dir_commands as dc


def menu():
    print('Выберете действие (1-4):')
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')
    print('Для выхода введите "q"')
    action = input()
    return action


def handler(action):
    if action == 'q':
        print('Выход из программы...')
        print('Успешно')
        return
    action_item = {
        '1': dc.change_dir,
        '2': dc.dir_list,
        '3': dc.del_dir,
        '4': dc.make_dir
        }
    item = None
    try:
        item = int(action)
        if item in range(1, 5):
            for item, key in action_item.items():
                if item == action:
                    key()
        else:
            print('"{}" - некорректная команда!'.format(action))

    except ValueError:
        print('"{}" - некорректная команда!'.format(action))

    answer = input('Продолжить работу с программой?\n"y" - Да: ')

    handler(menu()) if answer == 'y' else handler('q')


handler(menu())