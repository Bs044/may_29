sale = input('Введите сумму товара: ')
sale = int(sale)

if sale >= 200 and sale <= 300:
    print(f'Сумма к оплате со скидкой 3%: {sale - (sale / 100 * 3)}')
if sale >= 301 and sale <= 500:
    print(f'Сумма к оплате со скидкой 5%: {sale - (sale / 100 * 5)}')
if sale >= 501:
    print(f'Сумма к оплате со скидкой 7%: {sale - (sale / 100 * 7)}')
    