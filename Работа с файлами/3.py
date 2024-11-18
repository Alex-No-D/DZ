with open('input.txt','r') as f:
    a = []
    for i in f:
        a += [i.strip()]

    with open('output.txt', 'w') as f1:
        for i1 in range(len(a)):
            f1.write(f'{a[i1].upper()}\n')

