bools = [True,False]
print('x y z w')
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if ((not y or z) and (not(not (y or w) or (z and x)))) is True:
                    print(int(x),int(y),int(z),int(w))