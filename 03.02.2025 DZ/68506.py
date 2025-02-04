for i in range(1,1000):
    b = str(bin(i)[2:])
    if i % 2 ==0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    r = int(b,2)
    if r > 516:
        print(i)
        break