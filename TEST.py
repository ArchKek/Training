# int
# number = 228
# age = 19

# float
# number =228.228

# str
# name = "kek"
# name = 'kek'

# bool
# status = true
# status - false

# Экранирование
# print("он \"плохой\" человек")
# print('он "плохой" человек')

# Перевод строки
# print('Привет \n мир')
#
# print('Привет')
# print('мир')

# Конкатенация
# print("Привет, меня зовут" + name)
# print(" Мне " + str(age) + "лет")

# Ввод
# name = input("имя")
# age = input('age')

# print('Hello ' + name + ' your age is ' + age)

# + - * / ** % унарный минус, округление, Пи

# a = 5
# b = 25

# c = a + b  # сложение
# d = a - b  # вычитание
# e = a / b  # деление
# f = a * b  # умножение
# g = a ** 2  # возведение в степень
# k = b % 3  # деление по модулю
# a = -a  # унанрый минус

# a2 = 5.228
# print(round(a2))  # округление

# import math #импорт модуля
# print( math.pi ) #число пи

# kek = 1
# del(kek) # удаление переменной
# print(kek) # вывод

# метасинтаксические переменные
# foo
# bar

# уместные операторы (In-Place)
# kek = 10
# kek += 10
# print(kek)

# табуляция
# k = 'hello\tdaun'
# print(k)

# сепаратор
# x = 2
# z = 45
# print(x, z, sep=':')
# 2:45

# Если / условие
# if x>0:
#    smh
#    smh
# elif kek>0:
#    ...
# else: ....

# while цикл
# x = 1 # start
# while x < 101: # stop (заголовок цикла)
#    x += 1 # step
#    print(x)
# else
#    print('kok')

# Цикл for
# for x in 1, 1, 1, 1 : # кортеж (интерируемый объект)
# print(x)
# for x in range(start,stop,step):
# A = range(1,101,1)
# for x in A:
#    print(x)
# A[5] # вывод элемента

# функция
# def f(x, y): # x, y - формальные параметры
#   return x+y
# print (f(1,2))
# print (f(1,f(2,3)))

# def p3(x):
#   print(x)
#   print(x)
#   return # = return None
#   print(x)
# x = p3('hello')
# type(x) # Nonetype
# def f(x:int, y:int) ->int: # Type annotation(Аннотация типов)
# def plus(x;y):
#   'складывает x и y'


# \n \t \\
# s="""kek
# kek
# kek"""

# x = int(input()) # определение в каокй четверти находятся числа x,y
# y = int(input())
# if x > 0:
#    if y > 0: # x>0 y>0
#        print('I')
#    else:
#        print('IV') # x>0 y<0
# else:
#    if y>0: # x<0 y>0
#        print('II')
#    else: # x<0 y<0
#        print('III')
# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#    print("Первая четверть")
# elif x < 0 and y > 0:
#    print("Вторая четверть")
# elif x < 0 and y < 0:
#    print("Третья четверть")
# elif x > 0 and y < 0:
#    print("Четвертая четверть")
# else:
#    print("Точка находится на осях или в центре координат.")

# import turtle # черепаха
# def tr(a) # треугольник
#   for i in range 3:
#        kek.color(colors[i%3]) # цвет
#        kek.foward(a)
#        kek.left(60)

# colors=['green','red','blue'] #цвета
# kek = turtle.Turtle()
# kek.speed = 228 # скорость
# length = 25
#   for i in range(15):
#       tr(length)
#       kek.right(10)
#       length+=10

# Списки
# A = [1, 2, '3',(228. 332), [1000,2000], True]
# B = A # синоним
# A = [1, 2, 3]
# B = A
# B[0] = 10
# print(A) # [10, 2, 3]
# B = list() #<- любой итерируемый объект
# x = int('AB', base = 16) # конструктор
# B = list('Hello') #['H', 'e', 'l'. 'l', 'o']

# list - список [] меняется
# tuple - котреж () не меняется

# A =[1, 2, 3]
# A.append(4)
# A.append(A) # будет хранить ссылку на A
# print(A) # [1, 2, 3, 4,[...]]
# x = 2
# y = 2
# print(x is y) # True
# A = list(range(1,100,1))
# B = []
# for x in A:
#    if x%7==0:
#        B.append(x)
# print(B)
# B=[x for x in A if x%7==0]
# A,insert(x,1)

# k = [x for x in range(1,1000) if x%3==0 or x%5==0]
# print(sum(k))

#########################################

# f1, f2, s = 0, 1, 0
# while f2<4000000:
#    s = s + f2 if f2 % 2 == 0 else s
#    f1, f2 = f2, f1 + f2
#
# print(s)

#########################################