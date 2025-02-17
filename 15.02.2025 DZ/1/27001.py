bools = [True,False]
print('x y z w')
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if ((x and y and (not z) ) == (y or z or (not w))) is True:
                    print(int(x),int(y),int(z),int(w))