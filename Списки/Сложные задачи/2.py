from random import randint
a = []
for i in range(10):
    a.append(randint(1, 10))
print(a)
max = 0
n = 0

zisla = []
for i in a:
    if a.count(i) == max and i not in zisla:
        zisla.append(i)
    if a.count(i) > max:
        zisla.clear()
        max = a.count(i)
        n = i
        kol = a.count(i)
        zisla.append(n)
print(f'числа, которые встречаются чаще всего: {zisla}\nмаксимальное количество одинаĸовых элементов: {kol}')
