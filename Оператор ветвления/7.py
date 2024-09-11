x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))

if x1 < 1:
    print('Ошибка')
elif x1 > 8:
    print('Ошибка')
elif y1 < 1:
    print('Ошибка')
elif y1 > 8:
    print('Ошибка')
elif x2 < 1:
    print('Ошибка')
elif x2 > 8:
    print('Ошибка')
elif y2 < 1:
    print('Ошибка')
elif y2 > 8:
    print('Ошибка')
else:
    if abs(x1 - x2) == 2:
        if abs(y1 - y2) == 1:
            print('YES')
        else:
            print('NO')
    elif abs(x1 - x2) == 1:
        if abs(y1 - y2) == 2:
            print('YES')
        else:
            print('NO')




