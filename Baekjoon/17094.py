# 17094번 Serious Problem

l = int(input())
s = list(input())
a = 0
b = 0

for _ in range(0, l):
    if s[_] == '2':
        a += 1
    elif s[_] == 'e':
        b += 1

if a > b:
    print(2)
elif b > a:
    print('e')
else:
    print('yee')