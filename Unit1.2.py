# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 17:18:30 2025

@author: MrAng
"""


"""
Шенгенский калькулятор
"""
"""
Вариант написанный на лекции 1.1

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
"""
#Вариант на лекции 1.2

"""
#Вариант 1(для примера)

residence_limit = 90 # 45, 60
shegen_constraint = 180
visits = [[1,10],[30,54],[60,89],[120,159]]# в этой версии визиты задаются списками
#это двумерный список дат [[приехал, уехал], [приехал, уехал]]
total_time_in_es = 0
for visit in visits:
    total_time_in_es += visit[1] - visit[0] + 1#в цикле += прибавляет к самой переменной слева значение справа от оператора
    #visit[1] или visit[0] - это второй и первый элемент списка через их индекс
    
    
overstay_time_in_es = total_time_in_es - residence_limit
print('Вы превысили время пребывания', overstay_time_in_es)
#assert является спецификцией, т.е. проверкой
assert (overstay_time_in_es == 10 + 25 + 30 + 40 - residence_limit)
"""
#Вариант 2(для работы)

residence_limit = 90 # 45, 60
shegen_constraint = 180
visits = [[1,10],[61,90],[101,140],[141,160]]
days_for_visits = []
total_time_in_es = 0
for visit in visits:
    days_for_visit = 0
    for past_visit in visits:
        if past_visit[0] < visit[0]:
            #считаем визиты вплоть до текущего
            days_for_visit += past_visit[1] - past_visit[0] + 1
    days_for_visit += visit[1] - visit[0] + 1
    days_for_visits.append(days_for_visit)# append добавляет новое значение в список
print(days_for_visits)
assert(days_for_visits == [10,10 + 30,10 + 30 + 40,10 + 30 + 40 + 20])

for visit, total_days in zip(visits, days_for_visits):
    if total_days > residence_limit:
        overstay_time = total_days - residence_limit
        print('Во время визита', visit, 'время пребывания превышено на',overstay_time, 'дней')
        

   
    