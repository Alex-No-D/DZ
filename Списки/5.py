a = list(input('ввод: ') )
print(a)
if 'a' in a:
    a.remove('a')
if 'e' in a:
    a.remove('e')
if 'o' in a:
    a.remove('o')

print(a)