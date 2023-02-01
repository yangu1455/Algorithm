# 11650번 좌표 정렬하기

import sys

N = int(sys.stdin.readline())
coord = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    coord.append((x, y))

coord.sort()

for i in coord:
    print(i[0], i[1])