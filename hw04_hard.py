import re
# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

matrix_rotate = [list(x) for x in list(zip(*matrix))]

print(matrix_rotate)

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:

def prod_int(number_str):
    prod = 1
    for nums in number_str:
        for num in nums:
            prod *= int(num)
    return prod

number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

number_dict = {prod_int(nums): nums for nums in re.findall(r'\d{5}', number)}

res = [(number.index(value), key) for key,value in number_dict.items() if
       key == max(number_dict)].pop()

print('Индекс: {i}\n' \
      'Произведение: {prod}'.format(i = res[0], prod = res[1]))

# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

def arrang_chess(matrix, *adresses):

    for adress in adresses:
        i = 8 - adress[1]
        j = adress[0] - 1

        try:
            matrix[i][j] = 1
        except IndexError:
            print('ОШИБКА! Ферзь {} за пределами доски...'.format(adress))
            return

    return matrix


def iscrossing(matrix):

    res = 'No'

    try:
        for line in matrix:
            if line.count(1) != 1:
                return res
        for col in list(zip(*matrix)):
            if col .count(1) != 1:
                return res
    except TypeError:
        res = 'Исправьте адрес и попробуйте снова'
        return res

    res = 'Yes'

    return res

f1, f2, f3, f4, f5, f6, f7, f8 = ((1, 2), (2, 4), (3, 6), (4, 8),
                                  (5, 3), (6, 1), (7, 7), (8, 5))

chessboard = [[0]*8 for _ in range(8)]

chessboard = arrang_chess(chessboard, f1, f2, f3, f4, f5, f6, f7, f8)

if chessboard:
    print('''
    1  2  3  4  5  6  7  8
8  {line1}
7  {line2}
6  {line3}
5  {line4}
4  {line5}
3  {line6}
2  {line7}
1  {line8}
'''.format(line1=chessboard[0],
           line2=chessboard[1],
           line3=chessboard[2],
           line4=chessboard[3],
           line5=chessboard[4],
           line6=chessboard[5],
           line7=chessboard[6],
           line8=chessboard[7]))

res = iscrossing(chessboard)
print(res)