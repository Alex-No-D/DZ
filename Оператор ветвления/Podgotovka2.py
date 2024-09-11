x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))


k = (y2 - y1) / (x2-x1)

b = -x1 * k + y1
if b < 0:
     print(f'y={k}x - {-b}')
elif b > 0:
    print(f'y={k}x + {b}')
else:
    print(f'y={k}x')
