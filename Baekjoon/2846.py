# 2846번 오르막길

N = int(input())
Pi = list(map(int, input().split()))

res = []
h = 0

for i in range(1, N):
    if Pi[i]>Pi[i-1]:
        h+= Pi[i]-Pi[i-1]
        if i == N-1:
            res.append(h)
    else:
        res.append(h)
        h = 0

print(max(res))