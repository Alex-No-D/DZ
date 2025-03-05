p = [i for i in range(130,172) ]
q = [i for i in range(150,186) ]
BC = [130,171,150,185]
r = []
for s in BC:
    for e in BC:

        f = True
        a = [i for i in range(s , e + 1)]

        for x in range(0,1000):
            P = x in p
            Q = x in q
            A = x in a

            f = P <= ((Q and (not(A))) <= (not(P)) )
            if f is False: break
        if f: r.append(e - s)
print(min(r))
