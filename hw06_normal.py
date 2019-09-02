import random
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

FAMILY = ('Сидоров', 'Иванов', 'Петров', 'Осин', 'Волин', 'Сергеев', 'Дмитриев', 'Турин', 'Ткачев', 'Захаров', 'Лунев')
NAME = ('Ф.', 'А.', 'Д.', 'С.', 'Л.', 'В.', 'П.', 'Я.', 'Н.', 'Е.')
SUBJECT = ('математика', 'русский язык', 'физика', 'английский язык', 'химия', 'биология')


class School():
    def __init__(self, name):
        self.name = name
        self.Classes = []

    def addClass(self, Clas):
        self.Classes.append(Clas)

    def showClasses(self):
        print('Школа {} содержит:'.format(self.name))
        for itm in self.Classes:
            print('класс {}'.format(itm.name))

    def showClass(self, name):
        for itm in self.Classes:
            if itm.name == name: itm.showClass()

    def showPupilInfo(self, name):
        for cl in self.Classes:
            for pup in cl.Pupils:
                if pup.name == name:
                    for teach in cl.Teachers:
                        print('Ученик {} класс {} преподаватель {} предмет {}'.format(pup.name, cl.name, teach.name,
                                                                                      teach.subject))

    def showPupilParents(self, name):
        for cl in self.Classes:
            for pup in cl.Pupils:
                if pup.name == name: pup.showParents()

    def genSchool(self, classes, pupils, subjects):
        for idx in range(int(classes)):
            xclass = Class(str(random.randint(1, 11)) + random.choice(('А', 'Б', 'В', 'Г')))
            self.addClass(xclass)
            for i in range(int(pupils)):
                xclass.addPupil(Pupil(random.choice(FAMILY) + ' ' + random.choice(NAME) + random.choice(NAME),
                                      random.choice(FAMILY) + ' ' + random.choice(NAME) + random.choice(NAME),
                                      random.choice(FAMILY) + 'а ' + random.choice(NAME) + random.choice(NAME)))
            for i in range(int(subjects)):
                xclass.addTeacher(random.choice(FAMILY) + random.choice(NAME) + random.choice(NAME),
                                  random.choice(SUBJECT))


class Class():
    def __init__(self, name):
        self.name = name
        self.Pupils = []
        self.Teachers = []

    def addPupil(self, pupil):
        self.Pupils.append(pupil)

    def addTeacher(self, name, subject):
        self.Teachers.append(Teacher(name, subject))

    def showClass(self):
        print('Класс {} содержит:'.format(self.name))
        for itm in self.Pupils:
            print('ученик {}'.format(itm.name))


class Pupil():
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother

    def showParents(self):
        print('Отец - {}, Мать - {}'.format(self.father, self.mother))


class Teacher():
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject