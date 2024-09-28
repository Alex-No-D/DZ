a = int(input('сколько хотите ввести чисел: '))
cet = 0
necet = 0
for i in range(1, a+1):
    b = int(input('введите число: '))
    if b % 2 == 0:
        cet += 1
    elif b % 2 != 0:
        necet += 1
print(f'Количество чётных чисел: {cet} \nКоличество нечётных чисел: {necet}')
