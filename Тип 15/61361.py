v = True
for A in range(1000,1,-1):
    if v is False:
        break
    for x in range(1,100):
        if v is False:
            break
        for y in range(1,100):
            if ((x+2* y > 48) or (y > x) or ( x + 3*y < A)) is False:
                print(A)
                v = False
                break