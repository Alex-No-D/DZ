from random import randint
a = []
for i in range(10):
    a.append(randint(1, 10))
print(a)
sum = 0
for i1 in range(len(a)):
    sum+= a[i1]
print(sum)

