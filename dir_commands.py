import os
import sys
import shutil


def dir_list():
    cur_path = os.getcwd()
    list_dir = os.listdir(cur_path)
    return list_dir


def make_dir(name_dir):
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(cur_path)
        print('Директория {} успешно создана'.format(name_dir))
    except WindowsError:
        print('Папка с таким именем уже существует')


def del_dir(name_dir):
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.rmdir(cur_path)
        print('Директория {} успешно удалена'.format(name_dir))
    except WindowsError:
        print('Не удаётся найти путь')


def copy_file():
    file_name = sys.argv[0]
    while file_name in os.listdir(os.getcwd()):
        file_name = file_name.split('.py').pop(0) + '_copy.py'
    cur_file = os.path.join(os.getcwd(), sys.argv[0])
    new_file = os.path.join(os.getcwd(), file_name)
    try:
        shutil.copy(cur_file, new_file)
    except:
        print('Ошибка!')