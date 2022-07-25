# 2068. 최대수 구하기

T = int(input())

for t in range(1, T+1):
    A = map(int, input().split())
    
    print(f'#{t} {max(A)}')