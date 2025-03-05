for A in range(1000,1,-1):
    k = 0
    for x in range(1,1000):
        if ((70 % A == 0) and ((x % 28 == 0) <= ((x % A != 0 ) <= (x % 21 != 0) ))) is True:
            k += 1
        else:
            break
    if k == 999:
        print(A)
        break