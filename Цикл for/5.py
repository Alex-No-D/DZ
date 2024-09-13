a = int(input('введите число: '))
s = 0
for i in range(a + 1):
    s += i / 10 + 1

print(s)