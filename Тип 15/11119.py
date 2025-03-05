P = [i for i in range(20,51) ]
Q = [i for i in range(30,66) ]
BC = [20,50,30,65]
r = []
for s in BC:
    for e in BC:
        f = True
        a = [i for i in range(s , e + 1)]
        for x in range(0,100):
            f = (x not in a) <= ((x in P) <= (x not in Q))
            if f is False: break
        if f: r.append(e - s)
print(min(r))

