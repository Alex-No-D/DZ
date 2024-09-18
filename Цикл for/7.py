x = int(input('введите x: '))
n = int(input('введите n: '))
s = 0
for i in range(1, n+1):
    d = 1 / x ** (2*i - 2)

    s += d

print(s)
