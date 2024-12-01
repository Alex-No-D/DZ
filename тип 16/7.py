# Тип 16
# №47220
from sys import setrecursionlimit
setrecursionlimit(2100)


def f(n):
    if n ==1: return 1
    if n > 1: return f(n-1) * n
print(f(2023)/f(2020))