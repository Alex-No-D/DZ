with open('data.txt','r') as f:
    a = []
    for i in f:
        a += i.split()
        print(a)
    with open('even_numbers.txt', 'w') as f1:
        for i1 in a:
            if int(i1) % 2 == 0:
                f1.write(f"{i1} ")

