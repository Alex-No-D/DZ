
for A in range(0,1000):
    k = 0
    for x in range(0,1000):
            if (((x & 77) != 0) <= (((x & 12) == 0) <= ((x & A) != 0)))  is  False:
                k += 1
                break


    if k == 0:
        print(A)
        break
