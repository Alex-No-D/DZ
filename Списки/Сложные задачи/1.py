from random import randint
a = []

for i in range(10):
    a.append(randint(1, 10))
print(a)
o = 0
for i in range(len(a)-1):
    if (a[i] > a[i-1]) and (a[i] > a[i+1]):
        o = a[i]
        index = i

print(f'индекс последнего локального максимума: {index}\nэлемент: {o}')