# 2776번 암기왕
# https://www.acmicpc.net/problem/2776
# https://jinho-study.tistory.com/691 - 풀이 참고

import sys

# 테스트케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # '수첩 1'에는 동규가 본 정수들
    # '수첩 1'에 적어 놓은 정수의 개수
    N = int(sys.stdin.readline())
    # '수첩 1'에 적혀 있는 정수들
    num1 = set(sys.stdin.readline().split())
    # '수첩 2'에는 연종이 기억대로 적은 정수들
    # '수첩 2'에 적어 놓은 정수의 개수
    M = int(sys.stdin.readline())
    # '수첩 2'에 적혀 있는 정수들
    num2 = list(sys.stdin.readline().split())

    for i in num2:
        if i in num1:
            print(1)
        else:
            print(0)


# ======================================================
# 이분탐색 문제라 이분 탐색 풀이도 찾음

def bs(li, n):
    s, e = 0, len(li)-1
    while s <= e:
        m = (s+e)//2
        if li[m] == n:
            return 1
        elif li[m] < n:
            s = m+1
        else:
            e = m-1
    return 0
        
for _ in range(int(input())):
    N = int(input())
    li1 = sorted(list(map(int, input().split())))
    M = int(input())
    li2 = list(map(int, input().split()))
    for n in li2:
        print(bs(li1, n))