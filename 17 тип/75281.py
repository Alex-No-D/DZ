with open('75281.txt','r') as f:
    a = [int(i.strip()) for i in f]
    count = 0
    max_n = 0
    maxe = max(a)
    mine = min(a)
    for i in range(len(a) - 2):
        cisla4 = 0
        ostat5 = 0
        ostat7 = 0
        b = a[i:i+3]



        for i in b:
            if  999 < i < 10000:
                cisla4 = 1
            if (i % 5) == (maxe % 5):
                ostat5 +=1
            if (i % 7) == (mine % 7):
                ostat7 +=1

        if cisla4 == 1 and ostat5 <= 1 and ostat7 >= 2:
            if max_n < ( b[0] + b[1] + b[2]):
                max_n = b[0] + b[1] + b[2]
            count += 1
print(count,max_n)
