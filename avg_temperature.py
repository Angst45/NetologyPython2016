# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 19:27:15 2025

@author: MrAng
"""

#temperature = [0, 2, -2, -5]
#теперь можно обращаться к файлу с данными(ФАЙЛ TXT Example1.7.py.txt)

temperature = []#пустой список- переменная

#'.strip()' -удаление пробелов с обеих сторон текста
with open('Example1.7.py.txt') as t:#открытие файла, где данные в столбик
#with open('Example1.7.py.2.txt') as t:#открытие файла где эти же данные в строку

    for line in t:
        
        #temperature.append(line)#получается результат в списке типа[-2\n,-3\n]-строковый формат
        # '\n'- символ переноса строки
        #чтобы ето не происходило, добавим - 'int'
        temperature.append(int(line))
        #print(line.split())
        #temperature.append(line.strip())
        #теперь можно воспользоваться методом extend
        #temperature.extend(line.split())
        #temperature.append(line.split())
         
print(temperature)   


avg = sum(temperature)/len(temperature)

"""
Как записать в файл список? Сейчас разберем
"""
temperature_deviation = []
for t  in temperature:
    temperature_deviation.append(t - avg)

# '\n'- символ переноса строки 
print('Средняя температура \n в Нижнем Новгороде: ', "%.2f" % avg)
#конструкция"%.2f" % avg-позволяет отформатировать результат avg до 2х знаков
with open('average_temperature.txt', 'w') as t_average_file:#'w'-записать файл write - записать
    t_average_file.write(str("%.2f" % avg))#переменная должна бвть строковой, не float(если ничего не будет написано, то будет float)
    
with open('temperature_deviation.txt', 'w') as t_deviation_file:
    #t_deviation_file.write(str("%.2f" % avg))
    for t in temperature_deviation:
        t_deviation_file.write("%.2f\n"%t)
       
        
    