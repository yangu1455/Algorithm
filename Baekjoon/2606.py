# 2606번 바이러스

from pprint import pprint

# 첫째 줄에는 컴퓨터의 수가 주어진다. # 정점의 갯수
N = int(input())
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. # 간선의 갯수
M = int(input())

graph2 = [[] * N for _ in range(N+1)]

for _ in range(M):
    # 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다. # 간선들
    u, v = map(int, input().split())
    graph2[v].append(u)
    graph2[u].append(v)

# pprint(graph2)  # 인접 리스트

# ----------------------------------------
# DFS

count = 0
visited = [False] * (N+1)

def dfs(start):
    global count
    visited[start] = True

    for i in graph2[start]:
        if visited[i] == False:
            dfs(i)
            count +=1
 
dfs(1)
print(count)