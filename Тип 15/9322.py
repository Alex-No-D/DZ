for A in range(1,1000):
    k = 0
    for x in range(1,1000):
        if ((x % A == 0) <= ((x % 21 != 0) + (x % 35 == 0))) is True:
            k += 1
        else:
            break
    if k == 999:
        print(A)
        break