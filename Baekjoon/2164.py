# 2164번 카드2

import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()

for i in range(1, N+1):
    dq.append(i)

while len(dq) > 1:
    # 제일 위의 숫자 없앰
    dq.popleft()
    # 그 다음 남은 수 중에서 제일 위에 있던 것을 일단 맨 뒤에 추가 시키고
    dq.append(dq[0])
    # 그 다음에 가장 위에 있던 그 수를 없앰
    dq.popleft()

print(dq[0])