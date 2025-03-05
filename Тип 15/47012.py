p = [i for i in range(69,92) ]
q = [i for i in range(77,115) ]
BC = [69,91,77,116]
r = []
for s in BC:
    for e in BC:

        f = True
        a = [i for i in range(s , e + 1)]

        for x in range(0,1000):
            P = x in p
            Q = x in q
            A = x in a

            f = P <= ((not(P == Q)) or (Q <= A))
            if f is False: break
        if f: r.append(e - s)
print(min(r))

