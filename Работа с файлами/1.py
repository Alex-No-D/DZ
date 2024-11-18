with open('text.txt','r') as f:
    kslov = 0
    kstrok = 0
    ksymvol = 0
    for i in f:
        print(i.strip())
        a = i.split()
        kstrok += 1
        kslov += len(a)
        for i1 in i:
            ksymvol += 1


print(f'\nКоличество слов: {kslov} \nКоличество строк: {kstrok} \nКоличество символов(включая пробелы): {ksymvol}')