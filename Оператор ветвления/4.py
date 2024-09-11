A = int(input('введите время: '))

if  5 <= A <= 11:
    print('утро')
elif 12 <= A <= 17:
    print('день')
elif 18 <= A <= 22:
    print('вечер')
elif 23 <= A < 24:
    print('ночь')
elif 0 <= A <= 4:
    print('ночь')
else:
    print('ошибка')