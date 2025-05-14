with open('68518.txt','r') as f:
    a = [int(i.strip()) for i in f]
    count = 0
    min_n = 999999
    maxp = -99999
    for i in a:
        if i % 19 == 0:
            if i < min_n:
                min_n = i

    for i in range(len(a) - 1):
        c = 0
        b = a[i:i+2]
        for i1 in b:
            if i1 % min_n == 0:
                c = 1
        if c == 1:
            count += 1
            if maxp < ( b[0] + b[1]):
                maxp = b[0] + b[1]

    print(count,maxp)
