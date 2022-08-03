# 2167번 2차원 배열의 합

# 2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 
# 배열의 (i, j) 위치는 i행 j열을 나타낸다.

# K개의 줄에 순서대로 배열의 합을 출력한다. 배열의 합은 231-1보다 작거나 같다.



import sys

# 첫째 줄에 배열의 크기 N, M이 주어진다. 
N, M = map(int, sys.stdin.readline().split())

# 다음 N개의 줄에는 M개의 정수로 배열이 주어진다. 
matrix1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 그 다음 줄에는 합을 구할 부분의 개수 K가 주어진다. 
K = int(input())

# 다음 K개의 줄에는 네 개의 정수로 i, j, x, y가 주어진다.
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    sum = 0

    # x좌표 범위
    for a in range(i-1, x):
		# y좌표 범위
        for b in range(j-1, y):
            sum += matrix1[a][b]
    
    print(sum)


# tutor : "누적합" 또는 "부분합"을 검색해보시면 힌트를 얻으실 수 있을 것 같네요. 
# 정말 획기적인 풀이를 접하실 겁니다.
# pypy3 로 제출하면 시간초과 안 뜬다!


n, m = map(int, input().split())
s = []
r = [[0]*(m+1) for _ in range(n+1)]

for _ in range(n):
    s.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        r[i][j] = s[i-1][j-1] + r[i-1][j] + r[i][j-1] - r[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(r[x][y]-r[x][j-1]-r[i-1][y]+r[i-1][j-1])