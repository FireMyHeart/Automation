def month_to_season(num_of_month):
    if num_of_month.isdigit():
        if int(num_of_month) in [12, 1, 2]:
            print('Зима')
        elif int(num_of_month) in [3, 4, 5]:
            print('Весна')
        elif int(num_of_month) in [6, 7, 8]:
            print('Лето')
        elif int(num_of_month) in [9, 10, 11]:
            print('Осень')
        else:
            print('Вы должны ввести целое число от 1 до 12')
    else:
        print('Формат ввода - целое число!')
num_of_month = input('Введите номер месяца\n')
month_to_season(num_of_month)