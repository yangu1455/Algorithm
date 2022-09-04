# 1002번 터렛

import math

T= int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 거리 구하는 공식(
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    a = r1 + r2
    b = abs(r1 - r2)
    
    # 류재명이 있을 수 있는 위치의 개수 무한대
    if r1 == r2 and d == 0 :
        print(-1)
    elif a == d or b == d :
        print(1)
    elif b < d < a :
        print(2)
    else:
        print(0)