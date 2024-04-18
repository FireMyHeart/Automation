flag = False
while flag == False:
    my_age = input('Enter your age\n')
    if my_age.isdigit()==False:
        print('Формат ввода - натуральное число!')
    else:
        flag = True
my_age = int(my_age)
print(f'Ваш возраст: {my_age}')
flag = input('У вас был день рождения в этом году? y - да, n - нет\n')
if flag ==  'n':
    my_age += 1
    print(f'Вам исполнится в этом году: {my_age}')
else:
    print(f'В этом году вам исполнилось {my_age}')