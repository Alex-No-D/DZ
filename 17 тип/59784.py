with open('59784.txt','r') as f:
    a = [int(i.strip()) for i in f]
    count = 0
    min_n = 999999
    max15 = 0
    for i in a:
        if i % 100 == 15:
            if i > max15:
                max15 = i

    for i in range(len(a) - 2):
        cisla4 = 0
        b = a[i:i+3]
        for i1 in b:
            if 999 < abs(i1) < 10000:
                cisla4 +=1
        if  (cisla4 == 1) and (sum(b) < max15):
            count += 1
            if min_n > ( b[0] + b[1] + b[2]):
                min_n = b[0] + b[1] + b[2]

    print(count,min_n)
