# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 12:10:01 2025

@author: MrAng
"""
#Создадим словарь - содержит ключи и их характеристики

#country_name = 'Thailand'
#country_sea = True

#country_2_name = 'Hungary'
#country_2_sea = False

#если не изветстен тип данных, для того есть type()
#print(type(country_1))
#Создание ноавого словаря
#new_dict = dict()#{}

#country_1 = {'name':'Thailand','sea':True}
#country_2 = {'name':'Hungary','sea':False} 

#для простоты понимания заменим наши переменные некиим списком

#Подход №1 - списки[] - словари внутри списка
"""
countries = [
    {'name':'Thailand','sea':True,'schengen':False,'average_temperature':30,
     'currency_rate':1.8,'currency':'Thai$'}, 
    {'name':'Hungary','sea':False,'schengen':True,'average_temperature':10,
     'currency_rate':0.3,'currency':'Cr'},
    {'name':'Germany','sea':True,'schengen':True,'average_temperature':5,
     'currency_rate':80,'currency':'EU'},
    {'name':'Japan','sea':True,'schengen':False,'average_temperature':15,
     'currency_rate':0.61,'currency':'Yen'}
    ] #этот словарь - как список
"""
#словарь стран лучше преобразовать в другом виде, для удобства

#Подход №2 - словари{} - словари внутри словаря

countries = {
    'Thailand':{'sea':True,'schengen':False,
                'average_temperature':30,
                'currency_rate':1.8,
                'currency':'Thai$'},
    'Hungary':{'sea':False,'schengen':True,
               'average_temperature':10,
               'currency_rate':0.3,
               'currency':'Cr'},
    'Germany':{'sea':True,'schengen':True,
               'average_temperature':5,
               'currency_rate':80,
               'currency':'EU'},
    'Japan':{'sea':True,'schengen':False,
             'average_temperature':15,
             'currency_rate':0.61,
             'currency':'Yen'},
    }






""" такая конструкция слодная, напишем в следующем абзаце проще
#выведем все страны которые в шенгене
for country in countries:
    if country['schengen'] and country['sea'] and country['average_temperature'] > 10:#для обращения к нужному элементу словаря, нужно указать имя ключа
            print(country['name'])
"""
"""
schengen_countries =[] 
sea_countries = []

#найдем пересечен ие стран, где и море и шенген
for country in countries:
    if country['schengen']:
        schengen_countries.append(country['name'])
    if country['sea']:
        sea_countries.append(country['name'])
    
print(sea_countries)
print(schengen_countries)
print(schengen_countries + sea_countries)
"""
#получается не удобно, страны начинают дублироваться 
#для удобства - нужны множества

# МНОЖЕСТВА - УДОБНАЯ СТРУКТУРА ДЛЯ ПЕРЕСЕЧЕНИЯ И ОБЪЕДИНЕНИЯ, ПОДДЕРЖИВАЕТ УНИКАЛЬНОСТЬ ЭЛЕМЕНТОВ
# Множества - уникальность элементов, но нет упорядоченности элементов

#ЗАМЕНИМ следующие две строки             

schengen_countries = set() 
sea_countries = set()

#теперь после замены списка словарей, на словарь словарей, необходимо изменить цикл

"""

#найдем пересечен ие стран, где и море и шенген
for country in countries:
    if country['schengen']:
        schengen_countries.add(country['name'])#для множеств add не append 
    if country['sea']:
        sea_countries.add(country['name'])
"""    
#print(sea_countries)
#print(schengen_countries)
#print('Страны в шенгене и с морем: ',schengen_countries & sea_countries)   
# & - значит - удовлетворяет и одному и второму условию - ПЕРСЕЧЕНИЕ

#измененный цикл булет выглядеть ниже после прошлого закоментированного 

for country_name,properties in countries.items():
    if properties['schengen']:
        schengen_countries.add(country_name)
    if properties['sea']:
        sea_countries.add(country_name)


#Форматирование вывода

#money_amount = 10000

#for country in countries:
    
    #currency_amount = money_amount/properties['currency_rate']  
    #print(country['name'],'у нас будет %.2f ' % currency_amount ,properties['currency'])
#существует конструкция - подстановки
#мы пишем строку в том виде, который нужер, а на месте числа пишем %s(s - подставить, как строку)
#затем чрез знак % пишем значение которое нужно подставить
#после знака % ставится буква означающая тип подставляемого выражения
# %.2f - значит что запись будет сокращаться до второго знака 
# f - float - число с плавающей запятой(десятичная дробь) 
  
sea_schengen_countries = schengen_countries & sea_countries

"""
for country_name in sea_schengen_countries:
    for country in countries:
        if country['name'] == country_name:
            print(country)
            break
"""
for country_name in sea_schengen_countries:
    print(country_name, countries[country_name])
   
        
#словарь стран лучше преобразовать в другом виде, для удобства, смотри вначале   




 
 
 
 
 