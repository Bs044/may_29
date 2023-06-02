string = input('Введите предложение или слово: ')
g = string.replace(' ', '')
g = g.upper()
d = g[::-1]
if g == d:
    print(f'{string}, является палиндромом')
else:
    print(f'{string}, не является палиндромом')