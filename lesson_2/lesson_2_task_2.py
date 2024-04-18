# функцию написала для корректного определения високосности года, т.к. деления на 4 недостаточно.
def is_year_leap(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

# проверяла 2000, 1900, 2024, 1988, 1987

year = int(input('Enter year\n'))   
result = is_year_leap(year)
print(f'Год {year}: {result}')