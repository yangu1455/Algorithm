# 1976. 시각 덧셈

T = int(input())

for x in range(1, T+1) :
    a, b, c, d = map(int,input().split())
    res1 = 0
    res2 = 0
    
    if b+d >= 60:
        res2 = (b+d) - 60
        res1 += 1
    else:
        res2 = b+d
    
    res1 += a+c
    
    if res1 >= 12:
        res1 -= 12

    print(f'#{x} {res1} {res2}')