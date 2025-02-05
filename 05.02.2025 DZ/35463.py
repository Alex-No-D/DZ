for N in range(100, 1000):
    p = bin(N)[2:]
    for v in range(3):
        k0 = p.count('0')
        k1 = p.count('1')

        if k0 == k1:
            p += p[-1]
        elif k1 > k0:
            p += '0'
        elif k1 < k0:
            p += '1'
    R = int(p,2)
    if R % 4 ==0:
        print(N)
        break