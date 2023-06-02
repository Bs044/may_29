number = input('Введите трехзначное число: ')
number1 = number[0]
number2 = number[1]
number3 = number[2]
if number1 == number2 or number2 == number3:
    print(number, 'совпадения найдены')
else:
    print('Совпадений нет')