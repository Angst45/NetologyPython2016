# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 19:30:25 2025

@author: MrAng
"""
residence_limit = 90 #45,60
shengen_constraint = 180
#ФУНКЦИИ - использование встроенных и создание собственных
#чтобы вызвать функцию - нужно задать ее имя и в скобках перечислить ее параметры

#работа по лекции на классной доске
#остановка лекции 0:24:17
#работа после остановки лекции здесь - продолжается шенгенский калькулятор

#улчшим код
#мы можем сосздать функцию для длины визита
#потому, что часто используется и не хочется ошибится

# Вариант 1
def date_difference(leave, arrive):
    #pass#означает пустую функцию/список/слово
    result = leave - arrive + 1
    return result
# Вариант 2
def visit_length(visit):# функция понимает длину visit
    return date_difference(visit[1], visit[0])

#теперь можно заменить все еще одной функцией
def get_days_for_visits(visits):
    days_for_visits = []
    for visit in visits:
        days_for_visit = 0
        for past_visit in visits:
            if visit[0] - shengen_constraint < past_visit[0] < visit[0]:
                days_for_visit += visit_length(past_visit)
        days_for_visit += visit_length(visit)
        days_for_visits.append(days_for_visit)
    return  days_for_visits
    


#теперь мы можем заменить все наши visit на date_difference
"""
residenct_limit = 90 #45,60
shengen_constraint = 180
visits = [[1,10],[61,90],[101,140],[141,160],[271,290]]
days_for_visits = []

for visit in visits:
    days_for_visit = 0
    for past_visit in visits:
        if visit[0] - shengen_constraint < past_visit[0] < visit[0]:
            days_for_visit += past_visit[1] - past_visit[0] + 1
    days_for_visit += visit[1] - visit[0] + 1
    days_for_visits.append(days_for_visit)
    
print(days_for_visits)
#assert (days_for_visits = [10,10+30,10+30+40,10+30+40+20,40+20+20])

for visit, total_days in zip(visits, days_for_visits):
    if total_days > residenct_limit:
        over_saty_time = total_days - residenct_limit
        print('Во время визита', visit, 'количество времени пребывания превышено на', over_saty_time, 'дней')
"""        

#ДЛЯ ВАРИАНТА 1
"""
residenct_limit = 90 #45,60
shengen_constraint = 180
visits = [[1,10],[61,90],[101,140],[141,160],[271,290]]
days_for_visits = []

for visit in visits:
    days_for_visit = 0
    for past_visit in visits:
        if visit[0] - shengen_constraint < past_visit[0] < visit[0]:
            days_for_visit += date_difference(past_visit[1], past_visit[0])
    days_for_visit += date_difference(visit[1], visit[0])
    days_for_visits.append(days_for_visit)
    
print(days_for_visits)
assert (days_for_visits == [10,10+30,10+30+40,10+30+40+20,40+20+20])

for visit, total_days in zip(visits, days_for_visits):
    if total_days > residenct_limit:
        over_saty_time = total_days - residenct_limit
        print('Во время визита', visit, 'количество времени пребывания превышено на', over_saty_time, 'дней')
"""
#ДЛЯ ВАРИАНТА 2

def print_residence_limit_violation(visits):

visits = [[1,10],[61,90],[101,140],[141,160],[271,290]]
days_for_visits = get_days_for_visits(visits)
    
print(days_for_visits)
assert (days_for_visits == [10,10+30,10+30+40,10+30+40+20,40+20+20])

for visit, total_days in zip(visits, days_for_visits):
    if total_days > residence_limit:
        over_saty_time = total_days - residence_limit
        print('Во время визита', visit, 'количество времени пребывания превышено на', over_saty_time, 'дней')

date_in_future = 310
days_in_es = 0



def print_days_futue_visit(visits,date_in_future)

    visits_for_future = visits + [[date_in_future,date_in_future]]
#используем объявленную функцию, что бы избавиться от кода(ниже закоменчен)
    days_for_future_visits = get_days_for_visits(visits_for_future)
    print(visits_for_future)

"""
days_for_future_visits = []
print(visits_for_future)
for visit in visits_for_future:
    days_for_visit = 0
    for past_visit in visits_for_future:
        if visit[0] - shengen_constraint < past_visit[0] < visit[0]:
            days_for_visit += visit_length(past_visit)
    days_for_visit += visit_length(visit)
    days_for_future_visits.append(days_for_visit)
"""

    days_in_es = residence_limit - days_for_future_visits[len(days_for_future_visits)-1]+1   
    print('Если въедем %s числа, сможем провести в шенгене %s дней' % (date_in_future,days_in_es))

    #при изменении кода assert помогает удостоверится, что код рабоатет, как раньше
    assert days_in_es == 90 - 20 -20
    #обратим внимание - этой фунции не нужен return
    
print_days_futue_visit(visits,date_in_future)

