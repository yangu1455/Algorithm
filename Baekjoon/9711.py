# 9711번 피보나치
# 파이썬으로는 시간초과 나올 가능성이 너무 높음!!!
# https://www.acmicpc.net/board/view/62825

# 문제
# 피보나치 수열은 아래와 같이 표현된다.
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 각 숫자는 앞의 두 숫자의 합으로 나타내는 것을 알 수 있다.
# P와 Q 그리고 n이 주어질 때, P번째 피보나치 숫자를 Q로 나눈 나머지를 구하여라. 

import sys

input = sys.stdin.readline

# 첫 번째 라인에는 정수 T개의 테스트 케이스가 주어진다.
T = int(input())
# 각 테스트 케이스는 정수 P와 Q가 주어진다.
P, Q = map(int, input().rstrip().split())

for x in range(1, None+1):

    # x는 테스트 케이스 번호(1부터 시작)
    # M = P번째 피보나치 숫자 % Q
    print("Case #{x}: {M}")