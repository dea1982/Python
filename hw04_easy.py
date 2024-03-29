# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list_a = [2, 78, 6, 8, 9, 12, 45, 923]
list_b = [a ** 2 for a in list_a]
print(list_b)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruts_1 = ['банан', 'апельсин', 'абрикос', 'киви', 'гранат']
fruts_2 = ['арбуз', 'яблоко', 'дыня', 'виноград', 'гранат', 'банан', 'киви']

fruts_common = [frut for frut in fruts_1 if frut in fruts_2]
print(fruts_common)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list_a = [-2, -16, 9, 24, 11, 81, 256, 111, 22]
list_result = [a for a in list_a if a > 0 and a % 4 != 0 and a % 3 == 0]
print(list_result)
