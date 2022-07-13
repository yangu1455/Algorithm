a, d, n = map(int, input().split())
res = a

for i in range(1, n) :
    res += d

print(res)