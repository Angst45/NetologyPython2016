# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 17:01:24 2025

@author: MrAng
"""
#пусть будет словарь
#рассказыает про крутую функцию pprint для красивого вывода данных
#для начала нужно импортировать модуль

from pprint import pprint


cities = {}

with open('week_temperature.txt') as f_week_temperature:
    #for line in f_week_temperature:#чтение файла построчно
     for city in f_week_temperature:
      #print(line)
       #попробуем зайти с другой стороны
       #print('city:', city)
       temperatures = f_week_temperature.readline()#позвоялет считывать строку из файла(по умолчанию длина в одну строку)
       #print('temp:', temperatures)
       cities[city.strip()] = temperatures.split()#удаляем переносы строк
#для каждого города,температуры в словаре городов, напечатать print
for city, temperatures in cities.items():
 
    avg = 0
    for t in temperatures:
        avg += int(t)
    avg = avg / len(temperatures)
    print(city,"%.2f" % avg)
#pprint(cities)        