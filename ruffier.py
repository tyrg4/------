''' Модуль для расчета результатов пробы Руфье.

Сумма измерений пульса в трех попытках (до нагрузки, сразу после и после короткого отдыха)
в идеале должна быть не более 200 ударов в минуту. 
Мы предлагаем детям измерять свой пульс на протяжении 15 секунд, 
и приводим результат к ударам в минуту умножением на 4:
    S = 4 * (P1 + P2 + P3)
Чем дальше этот результат от идеальных 200 ударов, тем хуже.
Традиционно таблицы даются для величины, делённой на 10. 

Индекс Руфье   
    IR = (4 * (P1 + P2 + P3) - 200) / 10
оценивается по таблице в соответствии с возрастом:
        7-8             9-10                11-12               13-14               15+ (только для подростков!)
отл.     < 6.5           < 5                 < 3.5               < 2                 < 0.5  
хор.    >= 6.5 и < 12   >= 5 и < 10.5       >= 3.5 и < 9        >= 2 и < 7.5        >= 0.5 и < 6
удовл.  >= 12 и < 17    >= 10.5 и < 15.5    >= 9 и < 14         >= 7.5 и < 12.5     >= 6 и < 11
слабый  >= 17 и < 21    >= 15.5 и < 19.5    >= 14 и < 18        >= 12.5 и < 16.5    >= 11 и < 15
неуд.   >= 21           >= 19.5             >= 18               >= 16.5             >= 15

для всех возрастов результат "неуд" отстоит от "слабого" на 4, 
тот от "удовлетворительного" на 5, а "хороший" от "уд" - на 5.5

поэтому напишем функцию ruffier_result(r_index, level), которая будет получать
рассчитанный индекс Руфье и уровень "неуд" для возраста тестируемого, и отдавать результат

'''
# здесь задаются строки, с помощью которых изложен результат:
txt_index = "Ваш индекс Руфье: "
txt_workheart = "Работоспособность сердца: "
txt_nodata = '''
нет данных для такого возраста'''
txt_res = []
txt_res.append('''низкая. 
Срочно обратитесь к врачу!''')
txt_res.append('''удовлетворительная. 
Обратитесь к врачу!''')
txt_res.append('''средняя. 
Возможно, стоит дополнительно обследоваться у врача.''')
txt_res.append('''
выше среднего''')
txt_res.append('''
высокая''')

def ruffier_index(P1, P2, P3):
    IR = (4 * (P1 + P2 + P3) - 200) / 10
    return IR
def neud_level(age):
    return 21-1.5*((min(15,age)//2))
def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    elif r_index >= level-4:
        return 1
    elif r_index >= level-9:
        return 2
    elif r_index >= level-14.5:
        return 3
    elif r_index<level-14.5:
        return 4
    
def test(P1, P2, P3, age,name):
    r_index = ruffier_index(P1,P2,P3)
    level = neud_level(age)
    string1 = f'''{name}
    Ваш индекс Руфье:{float(ruffier_index(P1,P2,P3))}
    Работоспособность сердца:{txt_res[ruffier_result(r_index, level)]}
    '''
    return string1

