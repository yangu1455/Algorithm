n , m, o = map(int, input().split())
cnt = 0

for i in range(n) :
  for j in range(m) :
    for k in range(o):
        print(i, j, k)
        cnt += 1

print(cnt)