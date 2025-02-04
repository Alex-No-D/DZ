bools = [True,False]
print('x y z w')
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if  ( (not (x==y) or (not(z) or w)) == (not((not w or x) or (not y or z)))) is True:
                    print(int(x),int(y),int(z),int(w))