game_name = 'В поисках Байта'

# храним алфавит в виде строки
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for char in gamer['name']:
    if char in alphabet:
        alphabet = alphabet.replace(char, '')
print(alphabet) 

# структура для хранения данных о пользователе и вопросы которые надо задать
player = {'name': {'question': 'Как тебя зовут?', 'answer': None},
          'age' : {'question': 'Сколько тебе лет?', 'answer': None},
          'sex': {'question': 'Какого ты пола? М/Ж', 'answer': None},
          'pet_name': {'question': 'Имя твоего питомца?', 'answer': None},
          'like_game': {'question': 'Любишь играть в игры? да/нет', 'answer': None}
          }

print('Добро пожаловать в игру', game_name)
"""
для того что-бы опросить нашего пользователя и в случае расширения опроса,
делаем цикл который пройдя по словарю будет задавать нужные вопросы
"""
for itm in player:
    '''
    вложеный бесконечный цикл очень опасен, надо его контролировать,
    он нужен для того что-бы снова задавать вопрос если мы получили неверные данные
    '''

    while True:
        # тут мы задаем вопрос добавляя перенос строки, и сохраняем во временную переменную
        temp = input(player[itm]['question'] + '\n')

        # преобразуем возраст в int
        if itm == 'age':
            if temp.isdigit():
                temp = int(temp)
            else:
                print('Надо вводить число')
                continue

        # проверяем пол
        elif itm == 'sex':
            # если в ответе пришло не м или ж сообщаем ошибку и запускаем цикл вопроса заного
            temp = temp.lower()
            if not (temp == 'м' or temp == 'ж'):
                print('Ваш пол надо вводить либо м либо ж')
                continue
        # тут мы проверяем ответ на да и нет, и преобразуем это в булевое значение
        elif itm == 'like_game':
            if temp == 'нет':
                temp = False
            elif temp == 'да':
                temp = True
            else:
                print('Вы должны ответить да или нет')
                continue

        # сохраняем ответ в структуру словаря
        player[itm]['answer'] = temp
        break

# проверяем возраст более 18, и основная логика игры у нас внутри

if player['age']['answer'] > 18:
    # данная переменная нужна что-бы учесть все ответы если пользователь очень старый для игры
    temp_answer = True
    if player['age']['answer'] >= 90:

        temp_question = ('Игра может быть слишком утомительна для вас, вы уверены что желаете играть? да/нет',
                         'Хорошо подумал? да/нет',
                         )

        for itm in temp_question:
            while temp_answer:
                temp_answer = input(itm + '\n')
                if temp_answer == 'да':
                    temp_answer = True
                elif temp_answer == 'нет':
                    temp_answer = False
                else:
                    print('Вы должны ответить да или нет')
                    continue
                if temp_answer:
                    print('Хорошо тогда начнем игру')
                else:
                    print('В другой раз, до свидания', player['name'['answer']])

                break
    else:
        print('Привет', player['name']['answer'])

    if temp_answer:
        print('Я могу назвать буквы алфавита которых нет в твоем имени')
        for char in alphabet:
            if char not in player['name']['answer']:
                print(char)

else:
    print('Тебе нельзя играть, слишком молодой') 