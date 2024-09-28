n = int(input('введите число n(от 1 до n): '))

for i in range(1,n+1):
    a0 = 0
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    a8 = 0
    a9 = 0
    pk = 0
    for i1 in str(i):
        if int(i1) == 0: a0 += 1
        elif int(i1) == 1: a1 += 1
        elif int(i1) == 2: a2 += 1
        elif int(i1) == 3: a3 += 1
        elif int(i1) == 4: a4 += 1
        elif int(i1) == 5: a5 += 1
        elif int(i1) == 6: a6 += 1
        elif int(i1) == 7: a7 += 1
        elif int(i1) == 8: a8 += 1
        elif int(i1) == 9: a9 += 1
        if a0 > 1 or a1 > 1 or a2 > 1 or a3 > 1 or a4 > 1 or a5 > 1 or a6 > 1 or a7 > 1 or a8 > 1 or a9 > 1:
            pk = 1
            break
    if pk == 1:
        continue
    print(i)

