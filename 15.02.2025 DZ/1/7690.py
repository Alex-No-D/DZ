for N in range(100,1000):
    p = str(N)
    p1 = str(int(p[0]) + int(p[1]))
    p2 = str(int(p[1]) + int(p[2]))
    a1 = str(max(int(p1),int(p2)))
    a2 = str(min(int(p1), int(p2)))
    if int(a1+ a2) == 157:
        print(N)
        break