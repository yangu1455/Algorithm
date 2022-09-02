# 10250번 ACM 호텔

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    f = n % h
    if n % h == 0:
        num = n//h
        f = h
    print(f*100+num)