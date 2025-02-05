bools = [True,False]
print('x y z w')
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if ((x and not(y) ) or (x == z) or w) is False:
                    print(int(x),int(y),int(z),int(w))