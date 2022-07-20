# 1284. 수도 요금 경쟁

T = int(input())

for x in range(1, T+1):
    p, q, r, s, w = map(int, input().split())
    res = 0

    a = w * p
    if w <= r :
        b = q
    else :
        b = q + (w - r) * s
    
    if a >= b:
        res = b
    else :
        res = a

    print(f'#{x} {res}')