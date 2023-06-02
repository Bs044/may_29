krug = input('Введите длину окружности: ')
perimetr = input('Введите периметр квадрата: ')
krug = int(krug)
perimetr = int(perimetr)
if perimetr > krug:
    print('Эта окружность поместиться в квадрат')
else:
    print('Такая окружность не поместиться в квадрат')