# 11050번 이항 계수 1

import sys

input = sys.stdin.readline().rstrip

N, K = map(int, input().split())

def fac(n):
    result = 1
    if n > 0:
        result = n * fac(n-1)
    return result

print(fac(N) // (fac(N-K) * fac(K)))