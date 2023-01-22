# 9659번 돌 게임 5
# https://www.acmicpc.net/problem/9659

# 돌은 1개 또는 3개 가져갈 수 있다. 마지막 돌 가져가는 사람이 이기고, 이기는 사람을 구하고, 상근 시작.

import sys

N = int(sys.stdin.readline())

if N % 2 == 0:
    print('CY')
else:
    print('SK')

# 입력 5
# 출력 SK