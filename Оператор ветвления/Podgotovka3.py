x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
x3 = int(input('x3: '))
y3 = int(input('y3: '))

A1 = (((x1 - x2)** 2) + ((y1 - y2)** 2) ) ** 0.5
A2 = (((x2 - x3)** 2) + ((y2 - y3)** 2) ) ** 0.5
A3 = (((x3 - x1)** 2) + ((y3 - y1)** 2) ) ** 0.5

if (A1 + A2) > A3:
    if (A2 + A3) > A1:
        if (A1 + A3) > A2:
            print('треугольник существует')
            if A1 == A2 == A3:
                print('и он равносторонний')
            elif A1 == A2:
                print('и он равнобедренный')
            elif A1 == A3:
                print('и он равнобедренный')
            elif A1 != A2 != A3:
                print('и он разносторонний')
else:
    print('такого треугольника не существует')