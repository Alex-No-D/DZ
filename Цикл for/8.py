count = 0
count13 = 0
for i in range(10 ** 6):
    l1 = i % 10
    l2 = i // 10 % 10
    l3 = i // 100 % 10
    r1 = i // 1000 % 10
    r2 = i // 10000 % 10
    r3 = i // 100000 % 10
    ls = l1 + l2 + l3
    rs = r1 + r2 + r3
    if ls == rs:
        count += 1
        if ls + rs == 13:
            count13 += 1

print(f'общее число счастливых билетов: {count} \nчисло счастливых билетов, у ĸоторых сумма цифр равна 13: {count13}')