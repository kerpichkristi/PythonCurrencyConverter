from forex_python.converter import CurrencyRates
from forex_python.converter import get_rate
from datetime import datetime
import requests
import re

f = open('forex.txt', 'w')

def text():
    global f
    f = open('forex.txt', 'a')
    timenow()
    f.write(timeon)
    f.write(lol + '\n')
    f.close()
    
def dostval():
    print('***********************')
    print("****Доступные валюты***")
    print("USD,EUR,RUB,GBP,RON")
    print("HKD,IDR,ILS,DKK,INR")
    print("THB,HRK,MYR,NOK,CNY")
    print("BGN,PHP,PLN,ZAR,CAD")
    print("ISK,BRL,AUD,HUF,SEK")
    print("CHF,MXN,CZK,SGD,NZD")
    print("TRY,JPY,KRW")
    print('***********************')

def loading():
    print("****Загрузка****")
    print('*')
    print('**')
    print('***')
    print('****')
    print('*****')
    print('******')
    print('*******')
    print('********')
    print('*********')
    print('**********')
    print('***********')
    print('************')
    print('*************')
    print('**************')
    print('***************')
    print('****************')
    print('*****************')
    print('******************')
    print('*******************')
    print('********************')
    print('*********************')
    print('**********************\n')

def converter():
    global lol
    print('')
    print("***Запуск конвертера***")
    print('***********************')
    cur = CurrencyRates()
    dostval()
    exchange1()    
    exchange2()    
    num()
    print("*****Cумма расчета*****")
    print('Конвертация из', a ,'в', b)
    print(cur.convert(a,b,c))
    timenow()
    lol = " Converted "+ a + " in " + b 
    text()
    print('\n')
    main()

def exchange1():
    global a
    a = input("*****Введите валюту: ")
    sum_arr = ['USD','EUR','RUB','GBP','HKD','IDR','ILS','DKK','INR','CHF','MXN','CZK','SGD','THB','HRK','MYR','NOK','CNY','BGN','PHP','PLN','ZAR','CAD','ISK','BRL','RON','NZD','TRY','JPY','KRW','AUD','HUF','SEK']
    if a in sum_arr:
        return a
    else:
        print("*****Вы ввели неправильное значение") 
        return exchange1()

def exchange2():
    global b
    b = input("*****Введите валюту в которую конвертировать: ")
    sum_arr = ['USD','EUR','RUB','GBP','HKD','IDR','ILS','DKK','INR','CHF','MXN','CZK','SGD','THB','HRK','MYR','NOK','CNY','BGN','PHP','PLN','ZAR','CAD','ISK','BRL','RON','NZD','TRY','JPY','KRW','AUD','HUF','SEK']
    if b in sum_arr:
        return b
    else:
        print("*****Вы ввели неправильное значение") 
        return exchange2()

def num():
    global c
    c = input("*****Введите сумму:  ")
    while type(c) != float:
        try:
            c = float(c)
        except ValueError:
            print("*****ВЫ ВВЕЛИ ТЕКСТ, ВВЕДИТЕ ЧИСЛО!")
            c = input("*****Введите сумму: ")
            continue
        if c != 0:
            print("")
            loading()
            return c
            break
        else:
            c == 0
            print("*****Вы ввели НОЛЬ!")
            return num()

def retro():
    global lol
    print('*********************')
    print("Если выдаст ошибку, значит нет данных")
    print("об этой валюте в базе данных за то время")
    print('*********************')
    global t
    year()
    mounth()
    day()
    exchange1()
    exchange2()
    t = datetime(y,m,d)
    loading()
    print("\n*****Cумма расчета*****")
    print('\n')
    print('Ретрокурс 1 ', a ,'к', b)
    print('на',t )
    print('\n')
    print(b, get_rate(a,b,t))
    print('\n')
    tretro()
    lol = " Converted "+ a + " in " + b + " for " + tret
    text()
    main()

def tretro():
    global tret
    tret = str(t)
    
def retrocurs():
    global lol
    print('*********************')
    print("Если выдаст ошибку, значит нет данных")
    print("об этой валюте в базе данных за то время")
    print('*********************')
    global t
    year()
    mounth()
    day()
    exchange1()
    cur = CurrencyRates()
    t = datetime(y, m, d)
    print('\n')
    loading()
    print("\n*****Cумма расчета*****")
    print('Ретрокурс 1', a, " =")
    print("на", t )
    print('\n')
    print(a, cur.get_rates(a,t))
    print('\n')
    tretro()
    lol = " Converted "+ a + " for " + tret
    text()
    main()
    
def year():
    global y
    y = input("\n****Введите год: ")
    while type(y) != int:
         try:
             y = int(y)
         except ValueError:
             print("****НЕВЕРНО\n")
             y = input("Введите год еще раз: ")
             continue
            
         if 2000<=y<=2019:
             return y
         else:
             print("Введите год от 2000 до 2019:\n")
             return year()
                
def mounth():
    global m
    m = input("****Введите месяц: ")
    while type(m) != int:
         try:
             m = int(m)
         except ValueError:
             print("****\nНЕВЕРНО\n")
             return mounth()
         if 1<=m<=12:
             return m
         else:
             print("Введите месяц от 1 до 12:\n")
             return mounth()

def day():
    global d
    d = input("****Введите день: ")
    while type(d) != int:
         try:
             d = int(d)
         except ValueError:
             print("****\nНЕВЕРНО\n")
             return day()
         if m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
             if 1<=d<=31:
                 return d
             else:
                 print("Неверное значение, в этом месяце 31 день:")
                 return day()
         elif m==1 or m==4 or m==6 or m==9 or m==11:
             if 1<=d<=30:
                 return d
             else:
                 print("Неверное значение, в этом месяце 30 дней:")
                 return day()
         elif y==2000 or y==2004 or y==2008 or y==2012 or y==2016 or y==2020:
             if m==2 and 1<=d<=29:
                 return d
             else:
                 print("В этом году у Февраля всего 29 дней, введи правильное значение:")
                 return day()
         elif m==2:
             if 1<=d<=28:
                 return d
             else:
                 print("В этом году у Февраля всего 28 дней, введи правильное значение:")
                 return day()
         else:
             return d
    
def main():
    global lol
    global choise
    print("\n*********Меню*********")
    print('**********************')
    print("№ 0 - Вывод соотношения валют")
    print("№ 1 - Запуск конвертера")
    print("№ 2 - Доступные валюты")
    print("№ 3 - Конвертер в ретроспективе")
    print("№ 4 - Курс в ретроспективе")
    print("№ 5 - Сессия")
    print("№ 6 - Выйти из программы")
    print('***********************')
    choise = input("Введите номер действия : ")
    while type(choise) != float:
        try:
            choise = float(choise)
        except ValueError:
            print("*****ВВЕДИТЕ ЧИСЛО!")
            return main()
        if choise == 0:
            print('**********************')
            print("Текущий курс по отношению к валюте:")
            print('**********************')
            exchange1()
            print("****Вычисляем:*****")
            loading()
            cur = CurrencyRates()
            print('Курс 1', a, " =")
            print('на',timeon )
            timenow()
            print(cur.get_rates(a),"\n")
            timenow()
            lol = " Converted "+ a 
            text()
            return main()
        elif choise == 1:
            converter()
        elif choise == 2:
            lol = " Available currencies"
            text()
            dostval()
            return main()
        elif choise == 3:
            print("*****\nКонвертер в ретроспективе\n")
            return retro()
        elif choise == 4:
            print("№ 4 - Курс в ретроспективе")
            return retrocurs()
        elif choise == 5:
            returnsession()
            return main()
        elif choise == 6:
            print("****ВЫХОД:*****")
            loading()
            print('**********************\n')
            lol = "exit"
            text()
            break
        else:
            print("*****\nВы ввели недопустимое значение.\n")
            return main()

def returnsession():
    f = open ("forex.txt", "r")
    for i in open('forex.txt'):
        print(i)

def timenow():
    global tnow
    global timeon
    tnow = datetime.now()
    timeon = str(tnow)

converter()  



