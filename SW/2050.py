# 2050번 알파벳을 숫자로 변환

l = list(input())
res = []

for i in l :
    a= ord(i)
    res.append(a-64)

print(*res)