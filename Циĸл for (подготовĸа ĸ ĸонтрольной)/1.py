n = int(input('введите число n(от 100 до n): '))


for i in range(100, n + 1):
    ab = float(0)
    b = float('1' + ((len(str(i))) * '0'))
    for i1 in str(i):

        ab += float(i1) / b
        b = b / 10

    ii = (ab * int('1' + ((len(str(i))) * '0')))
    if round(ii) == i:
        print(i)


