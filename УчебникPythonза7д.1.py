# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 14:50:08 2025

@author: MrAng
"""

#Функция input()
#Во время работы иерпретаор останавливается и ждет, когда введут данные
"""
sample = input('Which country do you belong to?: ')
print(sample + 'is a great country!')
"""
#input() может выводить подсказки, состоящие из нескольких строк
"""
prompt = 'This is simple question to know what you like'
prompt += '\nSo, please say your favorite place:'
example = input(prompt)
print(example + 'is a great place to visit')
"""
#ЭКРАНИРОВАННАЯ ПОСЛЕДОВАТЕЛБНОСТЬ И ЧТО ЭТО ТАКОЕ
#Это особые серии символов , предназначенные для быстрого форматирования данных
"""
\n - данные с новой строки
\т - вывод данных со следующей позиции табуляции
\b - удаляет символ перед курсором
"""
#Комментарии в PYthon
"""
'#' - служит для однострочного комментария, пишутся прямо в коде
""" """ - служит для многострочного комментария
"""
#Зарезервированные ключевые слова
"""
существуют зарезервированные слова, которве нельзя применять для переменных
"""
#Операторы Python
"""
a = 32
b = 34
print(a+b)
#здесь +,= - операторы, а 'a' и 'b' - операнды
"""
#разновидности операторов

#сложение - '+'
"""
x = 54
y = 34
z = x + y
print(z)
"""
#вычитание - '-'
"""
x = 54
y = 34
z = x - y
print(z)
"""
#умножение - '*'
"""
x = 54
y = 34
z = x * y
print(z)
"""
#деление - '/'
"""
x = 54
y = 34
z = x / y
print(z)
"""
#остаток от деления
# '%" -  оператор определяет остаток от целочисленного деления
"""
x = 7
y = 3
z = x % y
print(z)
"""
#целочисленное деление
#'//' - используется, когда не важна точность результата
"""
x = 12
y = 5
z = x // y
print(z)
"""
#Побитовые операторы
#Все высоко уровневые языки используют: AND(&),OR(|),XOR(^),NOT(~)
#Эти операторы работают по традиционноой(булевой) логике

#для перевода в шеснадцатиричный формат служит функция hex()

"""
n = int(input('Введите число: '))
hex_number = hex(n)
print(hex_number)
"""
"""
x = float(input('Введите X: '))
y = float(input('Введите Y: '))
z = float(input('Введите Z: '))

sample = x**2*(2*y+5*z)
print(sample)
"""








