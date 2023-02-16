# 24678번 돌무더기 게임 1
# https://www.acmicpc.net/problem/24678
# https://minwin.tistory.com/38 => 풀이 참고

# 세개의 수가 짝수인지 홀수인지 판단하면 됨
# 짝짝짝, 짝짝홀의 경우 짝수번의 시행을 거쳐 마지막에 도착하므로 승자는 R
# 짝홀홀, 홀홀홀의 경우 홀수번의 시행을 거쳐 마지막에 도착하므로 승자는 B

import sys

input = sys.stdin.readline

# 테스트 케이스의 개수
T = int(input().rstrip())

for i in range(T):
    h = 0
    zz = 0
    # x, y, z 정수를 리스트로 받는 것이 편하다.
    xyz = list(map(int, input().rstrip().split()))
    # 3개의 정수
    for i in range(3):
        # 들어온 수가 짝수인 경우
        if xyz[i] % 2 == 0:
            zz += 1
        # 들어온 수가 홀수인 경우
        else:
            h += 1

    # 짝수가 2, 3개 들어오면 승자는 R
    if (zz == 3 or zz == 2):
        print('R')
    # 그 외의 경우 B
    else:
        print('B')
