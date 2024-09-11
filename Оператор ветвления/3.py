A = int(input('введите длину отрезка 1: '))
B = int(input('введите длину отрезка 2: '))
C = int(input('введите длину отрезка 3: '))
if (A + B) > C:
    if (A + C) > B:
        if (B + C) > A:
            print('YES')
        else:
            print('NO')