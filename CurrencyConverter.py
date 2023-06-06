from forex_python.converter import CurrencyRates, get_rate
from datetime import datetime

def text():
    with open('forex.txt', 'a') as f:
        f.write(timeon)
        f.write(lol + '\n')
    
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
    for i in range(1, 25):
        print('*' * i)
    print('**********************\n')

def converter():
    print('')
    print("***Запуск конвертера***")
    print('***********************')
    cur = CurrencyRates()
    dostval()
    a = exchange1()    
    b = exchange2()    
    c = num()
    print("*****Cумма расчета*****")
    print('Конвертация из', a ,'в', b)
    print(cur.convert(a, b, c))
    timenow()
    lol = " Converted "+ a + " in " + b 
    text()
    print('\n')
    main()

def exchange1():
    a = input("*****Введите валюту: ")
    sum_arr = ['USD', 'EUR', 'RUB', 'GBP', 'HKD', 'IDR', 'ILS', 'DKK', 'INR', 'CHF', 'MXN', 'CZK', 'SGD', 'THB', 'HRK', 'MYR', 'NOK', 'CNY', 'BGN', 'PHP', 'PLN', 'ZAR', 'CAD', 'ISK', 'BRL', 'RON', 'NZD', 'TRY', 'JPY', 'KRW', 'AUD', 'HUF', 'SEK']
    if a in sum_arr:
        return a
    else:
        print("*****Вы ввели неправильное значение") 
        return exchange1()

def exchange2():
    b = input("*****Введите валюту в которую конвертировать: ")
    sum_arr = ['USD', 'EUR', 'RUB', 'GBP', 'HKD', 'IDR', 'ILS', 'DKK', 'INR', 'CHF', 'MXN', 'CZK', 'SGD', 'THB', 'HRK', 'MYR', 'NOK', 'CNY', 'BGN', 'PHP', 'PLN', 'ZAR', 'CAD', 'ISK', 'BRL', 'RON', 'NZD', 'TRY', 'JPY', 'KRW', 'AUD', 'HUF', 'SEK']
    if b in sum_arr:
        return b
    else:
        print("*****Вы ввели неправильное значение") 
        return exchange2()

def num():
    c = input("*****Введите сумму:  ")
    while True:
        try:
            c = float(c)
            if c != 0:
                print("")
                loading()
                return c
            else:
                print("*****Вы ввели НОЛЬ!")
                c = input("*****Введите сумму: ")
        except ValueError:
            print("*****ВЫ ВВЕЛИ ТЕКСТ, ВВЕДИТЕ ЧИСЛО!")
            c = input("*****Введите сумму: ")

def retro():
    print('*********************')
    print("Если выдаст ошибку, значит нет данных")
    print("об этой валюте в базе данных за то время")
    print('*********************')
    year_val = year()
    month_val = month()
    day_val = day()
    a = exchange1()
    b = exchange2()
    t = datetime(year_val, month_val, day_val)
    loading()
    print("\n*****Cумма расчета*****")
    print('\n')
    print('Ретрокурс 1', a, 'к', b)
    print('на', t)
    print('\n')
    print(b, get_rate(a, b, t))
    print('\n')
    tret = str(t)
    lol = " Converted "+ a + " in " + b + " for " + tret
    text()
    main()

def retrocurs():
    print('*********************')
    print("Если выдаст ошибку, значит нет данных")
    print("об этой валюте в базе данных за то время")
    print('*********************')
    year_val = year()
    month_val = month()
    day_val = day()
    a = exchange1()
    cur = CurrencyRates()
    t = datetime(year_val, month_val, day_val)
    print('\n')
    loading()
    print("\n*****Cумма расчета*****")
    print('Ретрокурс 1', a, " =")
    print("на", t)
    print('\n')
    print(a, cur.get_rates(a, t))
    print('\n')
    tret = str(t)
    lol = " Converted "+ a + " for " + tret
    text()
    main()
    
def year():
    while True:
        try:
            y = int(input("\n****Введите год: "))
            if 2000 <= y <= 2019:
                return y
            else:
                print("Введите год от 2000 до 2019:\n")
        except ValueError:
            print("****НЕВЕРНО\n")

def month():
    while True:
        try:
            m = int(input("****Введите месяц: "))
            if 1 <= m <= 12:
                return m
            else:
                print("Введите месяц от 1 до 12:\n")
        except ValueError:
            print("****\nНЕВЕРНО\n")

def day():
    while True:
        try:
            m = int(input("****Введите месяц: "))
            d = int(input("****Введите день: "))
            if m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                if 1 <= d <= 31:
                    return d
                else:
                    print("Неверное значение, в этом месяце 31 день:")
            elif m == 1 or m == 4 or m == 6 or m == 9 or m == 11:
                if 1 <= d <= 30:
                    return d
                else:
                    print("Неверное значение, в этом месяце 30 дней:")
            elif y == 2000 or y == 2004 or y == 2008 or y == 2012 or y == 2016 or y == 2020:
                if m == 2 and 1 <= d <= 29:
                    return d
                else:
                    print("В этом году у Февраля всего 29 дней, введи правильное значение:")
            elif m == 2:
                if 1 <= d <= 28:
                    return d
                else:
                    print("В этом году у Февраля всего 28 дней, введи правильное значение:")
            else:
                return d
        except ValueError:
            print("****\nНЕВЕРНО\n")
        except UnboundLocalError:
            print("Сначала введите месяц.")

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
    choise = input("Введите номер действия: ")
    while True:
        try:
            choise = int(choise)
            if choise == 0:
                print('**********************')
                print("Текущий курс по отношению к валюте:")
                print('**********************')
                a = exchange1()
                print("****Вычисляем:*****")
                loading()
                cur = CurrencyRates()
                print('Курс 1', a, " =")
                print('на', timeon)
                timenow()
                print(cur.get_rates(a), "\n")
                timenow()
                lol = " Converted "+ a
                text()
                break
            elif choise == 1:
                converter()
            elif choise == 2:
                lol = " Available currencies"
                text()
                dostval()
                break
            elif choise == 3:
                print("*****\nКонвертер в ретроспективе\n")
                retro()
                break
            elif choise == 4:
                print("№ 4 - Курс в ретроспективе")
                retrocurs()
                break
            elif choise == 5:
                returnsession()
                break
            elif choise == 6:
                print("****ВЫХОД:*****")
                loading()
                print('**********************\n')
                lol = "exit"
                text()
                break
            else:
                print("*****\nВы ввели недопустимое значение.\n")
                choise = input("Введите номер действия: ")
        except ValueError:
            print("*****ВВЕДИТЕ ЧИСЛО!")
            choise = input("Введите номер действия: ")

def returnsession():
    with open("forex.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)

def timenow():
    global tnow
    global timeon
    tnow = datetime.now()
    timeon = str(tnow)

if __name__ == "__main__":
    print('*********************')
    print("****Курс валют******")
    print("********по*********")
    print("******Forex*******")
    print("*****конвертер*****")
    print('*********************')
    loading()
    print('\n')
    print('****Последняя сессия****')
    returnsession()
    main()