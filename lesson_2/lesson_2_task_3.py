from math import ceil


def square(a):
    return ceil(float(a) ** 2) #округление вверх до целого

a = input('Введите сторону квадрата\n')
print('Площадь квадрата равна:', square(a))

# Я сделала также свою функцию для корректного математического округления до целого числа. ceil() только вверх делает, round() почти идеален, но коряво считает, когда ровно 0.5 дробная часть. 
'''
def custom_round(a):
    if int(a) % 2 == 0 and abs(a - int(a)) == 0.5 and a > 0:
       return round(a) + 1
    elif int(a) % 2 == 0 and abs(a - int(a)) == 0.5 and a < 0:
        return round(a) - 1
    else:
        return round(a)
        
print(custom_round(6.5)) #7
print(custom_round(7.5)) #8
print(custom_round(-10.5)) #-11
print(custom_round(-7.5)) #-8
'''
#А потом я узнала, что round() округляет с любым количеством знаков после запятой, а ceil() так не работает, исключительно до целого вверх округляет. И что если нам надо с точностью, например 1 знак после запятой, то просто делаем не ceil(a), а ceil(a * 10) / 10. Отсюда родилась идея для усовершенствования моей самописной функции корректного математического округления.
'''
def math_round(a, b=0):
    a = a * (10 ** b)
    if int(a) % 2 == 0 and abs(a - int(a)) == 0.5 and a > 0:
       return (round(a) + 1) / (10 ** b)
    elif int(a) % 2 == 0 and abs(a - int(a)) == 0.5 and a < 0:
        return (round(a) - 1) / (10 ** b)
    else:
        return (round(a)) / (10 ** b)

print(math_round(3.55, 1)) #3.6
print(math_round(3.65, 1)) #3.7
print(math_round(3.5)) #4
print(math_round(4.5)) #5
'''
# Все работает, единственный момент, если до целого округляем, то на выходе float число, а не int. Не придумала, как это предусмотреть, не дублируя код.