bools = [True,False]
print('x y z w')
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if (((x and y) or (y and z)) == ((not x or w) and (not w or z))) is True:
                    print(int(x),int(y),int(z),int(w))