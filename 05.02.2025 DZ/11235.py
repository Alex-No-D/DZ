for i in range(1000,10000):
    p = str(i)
    p1 = str(int(p[0]) + int(p[1]))
    p2 = str(int(p[1]) + int(p[2]))
    p3 = str(int(p[2]) + int(p[3]))
    a1 = str(max(int(p1),int(p2),int(p3)))
    a2 = str(min(int(p1), int(p2),int(p3)))
    a0= str(int(p1) + int(p2) + int(p3) - int(a1) - int(a2))
    if int(a0+ a1) == 1418:
        print(i)
        break