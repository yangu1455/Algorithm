# 9660번 돌 게임 6

# https://ddggblog.tistory.com/150
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1,000,000,000,000)
# N의 범위가 너무 크기 때문에 DP로 풀거나 하면 메모리 초과가 떠버리구...

import sys

N = int(sys.stdin.readline())
# 0개, 1~4개까지는 결과 정하고 나머지(N에서 앞의 4칸을 제외한)는 0으로 채워두기
if N % 4 == 0:
    print("CY")
else:
    print("SK")