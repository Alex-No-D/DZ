def f(x,n):
    if x >= 67 and n ==2:
        return True
    elif (x>= 67 and n < 2) or (x < 67 and  n == 2 ):
        return False
    else:
        if n % 2 == 0:
            return f(x +1, n +1) and f(x+ 4,n +1) and f(x* 3, n+ 1)
        else:
            return f(x + 1, n + 1) or f(x + 4, n + 1) or f(x * 3, n + 1)
for x in range(1,67):
    if f(x,0):
        print(x)