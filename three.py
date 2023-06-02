year = input('Введите год: ')
year = int(year)
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f'Этот год високосный: {year}')
else:
    print(f'Этот год не високосный: {year}')