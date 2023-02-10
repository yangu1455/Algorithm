# 11399번 ATM문제

import sys

input = sys.stdin.readline

N = int(input())
time_list = list(map(int, input().rstrip().split()))

hap = 0
# 오름차순으로 정렬 후
time_list.sort()

# 합을 계산하면 최솟값이 나옴
for i in range(N):
    for j in range(i + 1):
        hap += time_list[j]

print(hap)