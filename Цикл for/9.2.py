stipendia = int(input('введите сумму стипендии в месяц: '))
rashodi = int(input('введите сумму расходов в месяц: '))
months = int(input('введите количество месяцев: '))
chet = input('первый месяц из суммы месяцев чётный ? (введите ДА или НЕТ): ')
ch = 0
sum = 0
if chet == "ДА":
    ch == 2
elif chet == "НЕТ":
    ch == 1
else:
    exit()
for i in range(1, months + 1):

    s = -(rashodi) + stipendia

    sum += s


    if (ch + 1) % 2 == 0:
        rashodi += rashodi / 100 * 5
    else:
        rashodi += rashodi / 100 * 3

if sum < 0:
    print(f'необходимая сумма для выживания: {round(abs(sum))} рублей')
else:
    print("для выживания начальных денег не потребуется")
