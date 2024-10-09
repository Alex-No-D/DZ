a = [1, 3, 4, 5]
b = [4, 5, 6, 7]
for i in a:
    if i in b:
        b.remove(i)
print(b)