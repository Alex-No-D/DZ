for N in range(1,101):
    o = bin(N)[2:]
    p = o[::-1]
    while p[0] == '0':
        p = p[1:]

    m = int(p,2)
    if m == 13:
        print(N)
