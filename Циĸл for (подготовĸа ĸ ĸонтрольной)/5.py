a = int(input('сколько хотите ввести чисел: '))
sum = 0
proiz = 1
sreda= 0
for i in range(1, a+1):
    b = int(input('введите число: '))
    sum += b
    proiz *= b
    sreda += b
sreda = sreda / a

print(f'Сумма всех чисел: {sum} \nПроизведение всех чисел: {proiz} \nCреднее арифметичесĸое чисел: {sreda}')