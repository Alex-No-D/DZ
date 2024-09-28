n = int(input('Количество участков: '))
t = 0
for i in range(1,n+1):
    l = int(input('длина данного участка (КМ): '))
    v = int(input('скорость на данном участке (КМ/Ч): '))
    t1 = l / v
    t += t1
print(f'время поездĸи: {round(t)} Ч ')

