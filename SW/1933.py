# 1933번 간단한 N 의 약수

N = int(input())
res = []

for i in range(1, N+1) :
    if N % i == 0:
        res.append(i)

print(*res)