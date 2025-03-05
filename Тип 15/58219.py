def d(n,m,k):
    if (n + m > k) and (k + m > n) and (n + k > m): return 1
    else: return 0




for A in range(1,100):
    k = True
    for x in range(1,10000):
            if (d(x,10,20) <= ((not(max(x,8) > 24)) == (not( d(3,A,x)))))  is  False:
                k = False
                break


    if k is True:
        print(A)

