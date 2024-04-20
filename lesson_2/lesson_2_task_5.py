flag = False
while not flag:
    num_of_month = input('Введите номер месяца\n')
    if num_of_month.isdigit()==False:
        print('Формат ввода - натуральное число!')
    if num_of_month.isdigit() and (int(num_of_month) > 12 or int(num_of_month) < 1):
        print('Вы должны ввести число от 1 до 12')
    elif num_of_month.isdigit() and int(num_of_month) in range(1, 13):
        flag = True

def month_to_season(num_of_month):
    if int(num_of_month) in [12, 1, 2]:
        print('Зима')
    elif int(num_of_month) in [3, 4, 5]:
        print('Весна')
    elif int(num_of_month) in [6, 7, 8]:
        print('Лето')
    else:
        print('Осень')

month_to_season(num_of_month)