A = int(input('введите номер дня недели: '))

if  1 <= A <= 5:
    print('Будни')
elif 6 <= A <= 7:
    print('Выходные')
else:
    print('ошибка')