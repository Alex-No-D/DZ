bools = [True,False]
print('x y z w')
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if (not (x == (not y)) or ((not z or (not w)) and (not w or y))) is False:
                    print(int(x),int(y),int(z),int(w))