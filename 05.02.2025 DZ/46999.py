bools = [True,False]
print('x y z w')
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if ((x == (not y or z)) and (not (not w) or (x==y))) is True:
                    print(int(x),int(y),int(z),int(w))