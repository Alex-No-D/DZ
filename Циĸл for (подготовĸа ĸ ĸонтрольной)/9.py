a = int(input('сколько денег всего: '))
r = int(input('исходная цена товара: '))
p = int(input('размер увеличения скидки после покупки каждого товара: '))
n = int(input('сколько товаров хотите купить: '))
p1 = 0
nc = 0
stop = False
for i in range(1, n+1):
    if a < (r - (r /100 * p1)) :
        print(f'\nБольше купить товаров нельзя \nу вас осталось денег: {a} \nвы купили {nc} товаров ')
        stop = True
        break
    else:
        a = a - (r - (r /100 * p1))
        nc += 1
        p1 += p
if stop == False:
    print(f'\nвы купили всё, что хотели \nУ вас осталось денег: {a}')
