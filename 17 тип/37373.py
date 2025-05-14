from itertools import *
with open('37373 .txt','r') as f:
    count = 0
    maxr = -9999
    a = [int(i.strip()) for i in f]
    for x in combinations(a,2):
        test13 = 0
        if (x[0] - x[1]) % 36 ==0:
            for i in x:
                if i % 13 == 0:
                    test13 = 1
                    break
            if test13 == 1:
                count +=1
                if x[0] - x[1] > maxr:
                    maxr = x[0] - x[1]
    print(count,maxr)


