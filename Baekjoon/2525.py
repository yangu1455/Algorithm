# 2525번 오븐 시계

a, b = map(int, input().split())
c = int(input())
d = a + (c//60)
e = b + (c%60)

if e > 59 :
    e -= 60
    d += 1
if d > 23 :
    d -= 24

print(d, e)