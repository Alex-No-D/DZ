from random import randint
a = []
for i in range(10):
    a.append(randint(1, 1000))
print(a)
max = 0
max2 =0
for i in a:
    if i > max:
        max2 = max
        max = i
    if (i < max) and (i > max2 ):
        max2 = i
print(f'первый максимум: {max}\nвторой максимум: {max2}')