
question1 = input('Сколько будет 2 + 2?: ')
question2= input('Сколько дней в году?: ')
question3 = input('Сколько стоит маленькая пачка чипсов Lays?: ')

question1 = int(question1)
question2 = int(question2)
question3 = int(question3)
    
count = 0
if question1 == 4:
    count += 2
if question2 == 365:
    count += 2
if question3 == 700:
    count += 2
print(f'Вы набрали {count} баллов')
