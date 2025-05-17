def f(x,y,n):
    if (x + y >= 67 and n == 2) or (x + y >= 67 and n == 4):
        return True
    elif (x+y >= 67 and n == 1 or (x+y >= 67 and n == 3)) or (x+y < 67 and n == 4):
        return False
    else:
        if n % 2 ==0:
            return f(x+1,y,n+1) and f(x,y+1,n+1) and f(x + y,y,n+1) and f(x,y+x,n+1)
        else:
            return f(x + 1, y, n + 1) or f(x, y + 1, n + 1) or f(x + y, y, n + 1) or f(x, y + x, n + 1)
def f1(x,y,n):
    if (x + y >= 67 and n == 2) :
        return True
    elif (x+y >= 67 and n == 1 ) or (x+y < 67 and n == 2):
        return False
    else:
        if n % 2 ==0:
            return f1(x+1,y,n+1) and f1(x,y+1,n+1) and f1(x + y,y,n+1) and f1(x,y+x,n+1)
        else:
            return f1(x + 1, y, n + 1) or f1(x, y + 1, n + 1) or f1(x + y, y, n + 1) or f1(x, y + x, n + 1)


for y in range(1,58):
    if f(9,y,0) == True and f1(9,y,0) == False:
        print(y)
        