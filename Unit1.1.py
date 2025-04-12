# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 16:06:56 2025

@author: MrAng
"""
"""
Шенгенский калькулятор
"""
residence_cost = 200

residence_limit = 90 #разрешенное время пребывания
shengen_constraint = 180 #ограничение на пребывание общее

first_time_arriving  = 5 #номер дня в году, когда приехали
first_time_leave = 17 # день когда уехали

second_time_arriving = 25
second_time_leave = 50

third_time_arriving = 75
third_time_leave = 112

#общее время пребывания
total_time_in_es = ((first_time_leave - first_time_arriving + 1) +
                    (second_time_leave - second_time_arriving +1) +
                    (third_time_leave - third_time_arriving +1))
#общие расходы
total_expenses = residence_cost * total_time_in_es
print('Дней в Евросоюзе',total_time_in_es, 'Дней')
print('Потратим',total_expenses, 'Евро')

#условия

if total_time_in_es == 77: # == - означает именно равенство
    print('Поездка в Италию в подарок')

if total_time_in_es > residence_limit: #ЕСЛИ
    #на сколько превышен?
    print('Лимит пребывания в Евросоюзе превышен')
    print('Пожалуйста выберите другие даты')
else: #ИНАЧЕ
    print('Не волнуйтесь, вы успеваете побыть в ЕС')

#СПИСКИ - ЭТО ИЗМЕНЯЕМЫЕ ПОСЛЕДОВАТЕЛЬНОСТИ    
    
month_accumulate_salary = 5 # количество месяцев для накопления    
man_salary = [1000, 1200, 1000, 1120, 700]# эта конструкция - список
woman_salary = [900, 1100, 1300, 600]
man_budget = sum(man_salary)#сумма чисел списка
print(man_budget)
woman_average_salary = sum(woman_salary)/len(woman_salary)#len - дает количество исмволов списка
woman_budget = woman_average_salary * month_accumulate_salary
common_budget = man_budget + woman_budget

if total_expenses < common_budget:
    print('Ура, едем!!!')
else:
    print('не едем :(')
    
    