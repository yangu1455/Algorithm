# 1712번 손익분기점

a, b, c = map(int, input().split())

if b >= c :
    print(-1)
else:
    print(a // (c - b) + 1)