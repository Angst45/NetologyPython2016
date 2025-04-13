# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 18:12:18 2025

@author: MrAng
"""
"""
height = float(input('Введите рост:'))
if height == 165:
    print('Ты танкист')
elif height > 165:
    print('Ты моряк')
elif height > 200:
    print('Дядя Степа')
else:
    print('Сиди дома')
"""
# and - обьединяет два условия
"""
x = int(input('x =  '))
if (x > 0) and (x < 15) :
    print('попал')
else:
    print('не попал')
"""    
#оператор or - или
"""
x = int(input('x =  '))
if (x > 0) and (x<10) or (x>20) and (x<30):
    print('попал')
else:
    print('не попал')
"""
#оператор in - проверяет вхождение, входит True, не входит False
"""
#эту запись запишем в консоли непосредственно и оно вернет True
height = 175
height in [165,170,175]
"""

#цикл for нужен для перебора итераций последовательно
"""
for i in [0,1,2,3,4]:
    print(i*2)

for i in 'string':
    print(i)
"""    
#в цикле for есть вспомагательные функции range(), enumerate()

#range() - задают диапазон значений или интервалы, можно использовать  непосредственно в цикле
#range() - можно задать диапазон и шаг (от кокого то числа,до кокого то числа, с шагом - каждое какое то число) - (0, 10, 2)
"""
iter_object = range(0,10,3)
for iteration in  iter_object:
    print(iteration)
"""
#enumerate() -для списка создает кортежи, где индекс итерируемого обьекта и сам обьект \
"""
i = [1,2,3,4,5,6,7,8]
res = enumerate(i)
print(res)
"""
#Цикл while - цикл с неизвестным количеством итераций(до бесконечности)
#работает с условиями  и пока условие выполняется не останавливается
#условия бывают True или False 
# while - пока
"""
height = 165
while height > 175:
#условия   
    print('рост = ', height)
    height += 1 #height = height + 1 - равнозначные надписи
#оператор break
    if height>200:#если условие выполнтлось то цикл завершится если написать дальше break
        break
"""
#оператор continue
"""
for i in range(30):
    if i == 2:
        continue
    print(i)#выводятся все числа списка но из-за continue
            #пропускается число 2
"""

#Функция zip склеивает списки, как застежка-молния(ZIP)
"""
a=[1,2,3]
b=[3,2,1]
print(list(zip(a,b)))
"""
#Функции - лекция 1.5
"""
def sum_numbers(a,b):
    c = a + b
    return c       
"""
#Функции len(), sum(),print()
"""
с=len([3,4,5])#
print(с) #выводит количество обьектов в массиве

d=sum([3,4,5])#сумма обьектов
print(d)
#ну а print() - принимает сколько угодно аргументов любых типов
"""
#что возвпащает фукнкция input(), она ждет введен7ные данные, вовдит строку
#что бы вводит числа нужны int() имли float()

"""
print('введи свое имя: ')
a = input()
print('Привет ',a)    
age = int(input('Введи свой возраст '))
print('Когда ты закончишь универ, тебе будет ', age + 5)
"""
"""
n = int(input('enter a number: '))

if 1<= n <=100:
    
    
    if n%2 != 0:
        print('Weird')
    if n%2 == 0 and 2<= n <=5:
        print('Not Weird')
    if n%2 == 0 and 6<=n<=20:
        print('Weird')
    if n%2 == 0 and n >20:
        print('Not Weird')
else:
    print('stop')
"""
"""
n = 10
l = [i for i in range(n)]
print(l)
"""    
"""
n = int(input('Введи длину списка: '))
if 1 <= n <= 20:
    l = [0]*n
    for i in range(n):
        l[i] = i
    for i in l:
        print(i*i)
else:
    print('stop')
"""
"""
n = int(input('Введи длину списка: '))
if 1 <= n <= 150:
  for a in  range(1,n+1):
      print(a, end='')
else:
    print('stop')   
"""


"""
if 1900<=year<=10**5:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print('True')
    else:
        print('False')
"""
"""
def is_leap(year):
   #leap = False    
   if 1900<=year<=10**5: 
     if year % 4 != 0 and (year % 100 == 0 or year % 400 != 0):
        
    # Write your logic here
    
        return leap
year = int(input('Введите год: '))
print(is_leap(year))
"""
"""
def is_leap(year):
   leap = False    
   if 1900<=year<=10**5: 
      return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        
    # Write your logic here
    
         
year = int(input('Введите год: '))
print(is_leap(year))
"""
 x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))

    

    
    
    

     
 

    
    
    
    