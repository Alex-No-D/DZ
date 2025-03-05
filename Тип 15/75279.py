
for A in range(0,100000):
    k = 0
    for x in range(0,100000):
            if ((((x & 6280) > 0) or ((x & 3394) > 0)) <= (((x & 10828) == 0) <= ((x & A) > 0))) is  False:
                k += 1
                break


    if k == 0:
        print(A)
        break
