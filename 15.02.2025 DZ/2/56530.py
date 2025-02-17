bools = [True,False]
print('x y z w')
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if (((not w or x) or ( not y or z)) and ( not (x == y) or (w == z))) is False:
                    print(int(x),int(y),int(z),int(w))