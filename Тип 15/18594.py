
for A in range(1000):
    v = True

    for m in range(1,100):
        if v is False:
            break
        for n in range(1,100):
            if (((2 * m + 3 * n) > 43) or ((m < A) or ( n <= A))) is False:


                v = False
                break
    if v is True:
        print(A)
        break