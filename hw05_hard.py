# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создание копии файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> - изменеие директории")
    print("ls - отображение полного пути")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def cp():
    if not dir_name:
        print("Необходимо указать имя копируемого файла вторым параметром")
        return
    c_file = dir_name
    while True:
        c_file = c_file.split('.py').pop(0) + '_copy.py'
        if c_file not in os.listdir(os.getcwd()):
            break
    cur_path_file = os.path.join(os.getcwd(), dir_name)
    copy_path_file = os.path.join(os.getcwd(), c_file)
    try:
        shutil.copy(cur_path_file, copy_path_file)
        print('файл {} успешно скопирован'.format(sys.argv[2]))
    except WindowsError:
        print('копирование невозможно!')


def rm():
    if not dir_name:
        print("Необходимо указать имя удаляемого файла вторым параметром")
        return
    confirm = input('Вы действительно хотите удалить\n' \
                    '"{}"? y/n: '.format(dir_name))
    if confirm == 'y':
        rm_file_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.remove(rm_file_path)
            print('Файл {} успешно удалён'.format(dir_name))
        except WindowsError:
            print('Невозможно удалить файл {}!\n' \
                  'такого файла не существует'.format(dir_name))


def cd():
    if not dir_name:
        print("Необходимо указать полный или относительный путь\n" \
              "к нужной директории вторым параметром")
        return

    if os.path.exists(dir_name):
        dir_path = dir_name
    else:
        dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print('Директория изменина')
    except WindowsError:
        print('Директории {}\n не существует!'.format(dir_name))


def ls():
    abs_dir_path = os.path.abspath(os.getcwd())
    print('Полный путь:\n{}'.format(abs_dir_path))


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")