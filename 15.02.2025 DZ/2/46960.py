bools = [True,False]
print('x y z w')
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if ((not (not y) or (z== w)) and ((not z or x) == w)) is True:
                    print(int(x),int(y),int(z),int(w))