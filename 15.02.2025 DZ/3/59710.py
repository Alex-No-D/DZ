for i in range(1,1000):
    b = str(bin(i)[2:])
    if i % 3 ==0:
        b = b + b[-3:]
    else:
        b =  b +  bin((i % 3 * 3))[2:]
    R = int(b,2)
    if R > 76:
        print(i)
        break