# 9661번 돌 게임 7

# 1~7까지 하나씩 해보고 결과에 규칙 있는 것 알아보기
# https://ddggblog.tistory.com/221

import sys

N = int(sys.stdin.readline())

if N % 5 == 0 or N % 5 == 2:
    print("CY")
else:
    print("SK")