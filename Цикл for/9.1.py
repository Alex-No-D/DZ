stipendia = int(input('введите сумму стипендии в месяц: '))
rashodi = int(input('введите сумму расходов в месяц: '))
months = int(input('введите количество месяцев: '))


sum = 0


for i in range(1, months + 1):

    s = -(rashodi) + stipendia

    sum += s


if sum < 0:
    print(f'необходимая сумма для выживания: {round(abs(sum))} рублей')
else:
    print("для выживания начальных денег не потребуется")