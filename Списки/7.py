from random import randint
a = []
for i in range(10):
    a.append(randint(1, 10))

a.sort()

print(a[-1])