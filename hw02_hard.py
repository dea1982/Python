# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5
y = 0
number = ''
stack = []
right_part = ''
for index, symbol in enumerate(equation):
    if symbol == '=':
        right_part = equation[(index + 1):]
        break

right_part = right_part.replace(' ', '')

for symbol in right_part:
    if symbol in '-+1234567890.':
        number += symbol
    elif number:
        stack.append(float(number))
        number = ''
        if symbol == 'x':
            stack[-1] = x * stack[-1]
if number:
    stack.append(float(number))

for number in stack:
    y = y + number

print('y = ', y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

answer = ''
while answer != 'n':
    answer = input('Приступим y/n: ')
    if answer == 'y':
        date = input('Введите дату в формате dd.mm.yyyy:')
        if len(date) == 10:
            dd, mm, yyyy = date.split('.')
            if len(dd) == 2 and len(mm) == 2 and len(yyyy) == 4:
                if dd.isdigit() and mm.isdigit() and yyyy.isdigit():
                    if (1 <= int(dd) <= 31) and (1 <= int(mm) <= 12) and (1 <= int(yyyy) <= 9999):
                        if dd == '31' and (mm in ['01', '03', '05', '07', '08', '10', '12']):
                            print('Дата: ', date)
                        elif int(dd) < 31:
                            print('Дата: ', date)
                        else:
                            print('Неверно указали день')
                            continue

                    else:
                        print('Неверно указали день')
                        continue
                else:
                    print('Вы ввели в неправильном формате: ')
                    continue
            else:
                print('Вы ввели в неправильном формате: ')
                continue
        elif len(date) < 10:
            print('Вы ввели мало цифр')
        elif len(date) > 10:
            print('Вы ввели слишком много цифр')
print('Пока')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
answer = ''

while answer != 'n':
    answer = input('Приступим y/n: ')
    if answer == 'y':
        index2 = 0
        n = 0
        floor = []
        room_floor = []
        room = int(input('Введит номер команты: '))
        if 1 <= room <= 2000000000:
            while n <= room:
                room_floor.append(n * n)
                room_floor[n] = room_floor[n] + room_floor[n - 1]
                floor.append(n)
                floor[n] = floor[n] + floor[n - 1]
                if room_floor[n] >= room:
                    index2 = room - (int((room - room_floor[n - 1]) / (floor[n] - floor[n - 1])) * (
                            floor[n] - floor[n - 1]) + room_floor[n - 1])
                    if index2 > 0:
                        index = floor[n - 1] + int((room - room_floor[n - 1]) / (floor[n] - floor[n - 1])) + 1
                    else:
                        index = floor[n - 1] + int((room - room_floor[n - 1]) / (floor[n] - floor[n - 1]))
                    break
                n += 1
            print('Этаж: ', index, 'Подъезд: ', index2, 'Команта: ', room)
        else:
            print('Вы ввели не верный номер')
            continue
