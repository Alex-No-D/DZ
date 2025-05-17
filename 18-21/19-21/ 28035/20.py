def f(x,n):
    if x >= 47 and n == 3:
        return True
    elif (x >= 47 and n < 3) or (x < 47 and n == 3):
        return False
    else:
        if n % 2 == 0:
            return f(x + 1,n+1) or f(x+2, n +1) or f(x* 2,n+1)
        else:
            return f(x + 1, n + 1) and f(x + 2, n + 1) and f(x * 2, n + 1)
for x in range(1,47):
    if f(x,0) == True:
        print(x)
        