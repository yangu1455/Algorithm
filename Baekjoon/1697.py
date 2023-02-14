# 1697번 숨바꼭질

# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# bfs(그래프 탐색) 문제~~!~!~!~!~
# https://chancoding.tistory.com/193
# https://wook-2124.tistory.com/273
# https://letalearns.tistory.com/34
# https://data-flower.tistory.com/78

import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

print(N, K)

res = N
second = 0
while res != K:
    x1 = res-1
    x2 = res+1
    x3 = 2*res
    if x1 == min(abs(K-x1), abs(K-x2), abs(K-x3)):
        res = x1
        second += 1
    elif x2 == min(abs(K-x1), abs(K-x2), abs(K-x3)):
        res = x2
        second += 1
    elif x3 == min(abs(K-x1), abs(K-x2), abs(K-x3)):
        rex = x3
        second += 1

print(second)



# ---------------------------------------------------

from collections import deque

n, k = map(int, input().split())
max_n = 100000

visited = [0] * (max_n + 1)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for j in (x-1, x+1, x*2):
            if 0 <= j <= max_n and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)

bfs()