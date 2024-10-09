from random import randint
a = []
b= []
for i in range(10):
    a.append(randint(1, 10))
print(a)
for i in a:
    if i not in b:
        b.append(i)
print(b)
print(f'кол-во различных элементов: {len(b)}')