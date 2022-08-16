# 4948번 베르트랑 공준

import sys

while True:
    n = int(sys.stdin.readline())
    count = 0
    res = []

    if n == 0:
        break

    # 소수인지 판별하는 함수
    def isPrime(a):
        # 1일 경우는 소수 판단도 안하고 바로 False 반환
        if a == 1 :
            return False
        else : 
            # 소수 판별 공식
            # 소수면 True 반환
            for i in range(2, int(a ** 0.5) + 1):
                if a % i == 0 :
                    return False
            return True

    for j in range(n+1, 2*n+1):
        if isPrime(j):
            count += 1

    print(count)