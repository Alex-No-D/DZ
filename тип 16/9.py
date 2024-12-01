# Тип 16
# №58226
def f(n):
    if n ==1: return 1
    if n == 2: return 2
    if n > 2 and n % 2 == 0: return int((3*n+f(n-3))/3)
    if n > 2 and n % 2 != 0: return int((7*n+f(n-1)-f(n-2)) / 5)
print(f(35))