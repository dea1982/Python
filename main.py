print('Вас приветствует Игра')
gamer = {'name': input('Как вас зовут?\n'),
         'age': int(input('Сколько вам лет?\n')),
         'sex': input('Ваш пол?\n'),
         'pet_name': input('Как зовут вашего питомца?\n'),
         'gemer_like': input('Любите ли вы играть?\n')
         }
if gamer['age'] < 18:
    print('Тебе нельзя играть')
elif gamer['age'] > 90:
    print('Для вас это может быть утомительно')
    i = 0
    while i < 2:
        a = input('Уверены, что хотите сыграть?\n')
        if a == 'Да':
            i += 1
            if i == 2:
                print('Хорошо тогда начнем игру')
                print('Добро пожаловать в Игру', gamer['name'])
                print('Я могу назвать буквы алфавита, которых нет в твоем имени')
        elif a == 'Нет':
            print('До свиданья, ', gamer['name'])
            break
elif gamer['gemer_like'] == 'Нет':
    print('До свиданья, ', gamer['name'])
else:
    print('Добро пожаловать в Игру', gamer['name'])
    print('Я могу назвать буквы алфавита, которых нет в твоем имени')

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for char in gamer['name']:
    if char in alphabet:
        alphabet = alphabet.replace(char, '')
print(alphabet)