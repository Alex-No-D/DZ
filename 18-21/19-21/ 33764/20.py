def f(x,y,n):
    if x + y >= 67 and n == 3:
        return True
    elif (x+y >= 67 and n < 3) or (x+y < 67 and n == 3):
        return False
    else:
        if n % 2 ==0:
            return f(x+1,y,n+1) or f(x,y+1,n+1) or f(x + y,y,n+1) or f(x,y+x,n+1)
        else:
            return f(x + 1, y, n + 1) and f(x, y + 1, n + 1) and f(x + y, y, n + 1) and f(x, y + x, n + 1)
for y in range(1,58):
    if f(9,y,0) == True:
        print(y)
       