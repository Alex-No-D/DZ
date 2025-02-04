for i in range(1,1000):
    b = str(bin(i)[2:])
    if i % 2 ==0:
        b += '10'
    else:
        b += '01'
    r = int(b,2)
    if r < 109:
        print(r)