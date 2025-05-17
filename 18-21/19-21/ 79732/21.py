def f(x,n):
    if x >= 67 and (n ==2 or n == 4):
        return True
    elif (x >= 67 and (n == 1 or n == 3)) or (x < 67 and  n == 4 ):
        return False
    else:
        if n % 2 == 0:
            return f(x +1, n +1) and f(x+ 4,n +1) and f(x* 3, n+ 1)
        else:
            return f(x + 1, n + 1) or f(x + 4, n + 1) or f(x * 3, n + 1)
def f1(x,n):
    if x >= 67 and (n ==2):
        return True
    elif (x >= 67 and (n == 1 )) or (x < 67 and  n == 2 ):
        return False
    else:
        if n % 2 == 0:
            return f1(x +1, n +1) and f1(x+ 4,n +1) and f1(x* 3, n+ 1)
        else:
            return f1(x + 1, n + 1) or f1(x + 4, n + 1) or f1(x * 3, n + 1)
for x in range(1,67):
    if f(x,0) and f1(x,0) == False:
        print(x)
        break