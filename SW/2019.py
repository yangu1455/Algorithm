# 2019번 더블더블

num = int(input())
res = []

for n in range(num+1):
    n = 2 ** n
    res.append(n)

print(*res)