# 1018번 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018


n, m = map(int, input().split())
# 받은 판
board = []
result = []
 
# board에 데이터 받기
for _ in range(n):
    board.append(input())
 
# (1, 1)잡기
for i in range(n-7):
    for j in range(m-7):
        # 시작점 리셋
        draw1 = 0
        draw2 = 0
 
        # 시작점부터 8*8판 범위
        for a in range(i, i+8):
            for b in range(j, j+8):
                # (짝, 짝) or (홀, 홀)인 경우 => 시작점의 색깔과 같아야한다.
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
 
        result.append(draw1)
        result.append(draw2)
 
print(min(result))