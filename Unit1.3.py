# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:58:10 2025

@author: MrAng
"""
"""

residence_limit = 90 # 54, 90
shengen_constraint = 180

first_time_arriving = 1
first_time_leave = 10

second_time_arriving = 21
second_time_leave = 30

third_time_time_arriving = 45
third_time_leave  = 46

fourth_time_arriving  = 91
fourth_time_leave = 100


total_time_in_es = (first_time_leave - first_time_arriving + 1)
total_time_in_es = total_time_in_es + (second_time_leave - second_time_arriving + 1)
total_time_in_es = total_time_in_es + (third_time_leave - third_time_time_arriving + 1)
total_time_in_es = total_time_in_es + (fourth_time_leave - fourth_time_arriving + 1)

#добавим assert - для проверки
#assert - показывает что мы ожидаем от программы 
#если интерпретатор дойдет до этой строки кода и результат не совпадет, то выпонение остановится
assert total_time_in_es == 10 + 10 + 2 + 10 #можно написать прото сумму, но лучше расписать


if total_time_in_es > residence_limit:
    print("Вы не можете пребывать в ЕС так долго")
    
print("Вы пробудете в ЕС дней: ", total_time_in_es )
"""
#Эту прграмму модно упростить, для этого понадобятся списки

residence_limit = 90 # 54, 90
shengen_constraint = 180


#visit_1 = [1,10] # Список = [день приезда, день отъезда]

#visit_2 = [21,30]

#visit_3 = [45,46]

#visit_4 = [91,100]

#можно для списка visits написать все переменные-списки visit_№ внутри
#visits = [visit_1, visit_2, visit_3, visit_4]#для упрощения понимания, список списков
visits = [[1,10],[21,30],[45,46],[100,349],[351,360],2]#специально вели 2, чтобы выявить ошибку, тюкю 2 - не список

for visit in visits:
    if not isinstance(visit, list):#проверяет является ли переменная объектом типа список или другим указанным классом
        raise Exception('Ошибка в типе поездки', visit)#кидает исключение и останавливает программу
                                                       #останавливает из-за ошибки 

days_in_eu = []#список пездок

total_time_in_es = 0#изначально мы не находились в ЕС  
#создадим цикл for
#нужно пройти по каждой поездке из массива поездок и прибавлять время нахождения в ЕС 
for visit in visits:
    
    past_days = 0 
    
    for past_visit in visits: #хотим нати все поездки, т.е. сложить их
    
        #if past_visit[0] <= visit[0] and past_visit[0] > visit[0] - shengen_constraint:#для того, что бы точно определить, что поездка предидущая  
        if visit[0] - shengen_constraint < past_visit[0] <= visit[0]:#эквивалентно верхнему условию   
            past_days += past_visit[1] - past_visit[0] + 1    
    days_in_eu.append(past_days)#добавим дни в ЕС(добавляет в конец списка элемент)
    total_time_in_es += visit[1] - visit[0] + 1
    
#после внесения этой зависимости код ниже можно закомментировать или удалить 
#теперь код можно переписать, используя имена списков
#total_time_in_es = (visit_1[1] - visit_1[0]+ 1)
#total_time_in_es += (visit_2[1] - visit_2[0]+1 )
#total_time_in_es += (visit_3[1] - visit_3[0]+1)
#total_time_in_es += (visit_4[1] - visit_4[0]+1)
 
#добавим assert - для проверки
#assert - показывает что мы ожидаем от программы 
#если интерпретатор дойдет до этой строки кода и результат не совпадет, то выпонение остановится
#assert total_time_in_es == 10 + 10 + 2 + 10 #можно написать прото сумму, но лучше расписать
#сейчас assert закомент для продолжения работы с кодом

print(days_in_eu)
print(visits)
#assert days_in_eu == [10,10+10,10+10+2,10]

for visit,days in zip(visits, days_in_eu):#для склеивания двух списков
    if days > residence_limit:
        print('В течении поездки', visit, 'Вы пребывали в ЕС слишком долго:', days)

if total_time_in_es > residence_limit:
    print("Вы не можете пребывать в ЕС так долго")
    
print("Вы пробудете в ЕС дней: ", total_time_in_es )




