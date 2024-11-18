with open('message.txt', 'r') as f:
    with open('encrypted_message.txt', 'w') as f1:
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in f:
            b = i.split()
            for i1 in b:
                slovo =''
                for i2 in i1:

                    zam = abc.index(i2) + 3
                    if zam > 25:
                        zam -= 26
                    slovo += abc[zam]
                f1.write(f'{slovo} ')

