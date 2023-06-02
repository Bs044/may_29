usd = input('Введите сколько долларов вы хотите обменять: ')
usd = int(usd)
valuta = input('В какую валюту вы хотите перевести "EUR, UAN, AZN": ')
if valuta == 'AZN' or valuta == 'azn':
    print(f'{usd}$ в AZN будет: {usd * 1.70}')
elif valuta == 'EUR' or valuta == 'eur':
    print(f'{usd}$ в EUR будет: {usd * 0.94}')
elif valuta == 'UAN' or valuta =='uan':
    print(f'{usd}$ в UAN будет: {usd * 7.13}')
else:
    print('Такая валюта недоступна!')