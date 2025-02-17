for i in range(1,13):
    b = str(bin(i)[2:])
    if i % 2 ==0:
        b = '10' + b
    else:
        b = '1' + b + '00'
    R = int(b,2)
    print(R)