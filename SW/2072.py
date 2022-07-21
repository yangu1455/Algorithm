# 2072. 홀수만 더하기

T = int(input())

for x in range(1, T+1):
    case = map(int, input().split())
    hap = 0
    for c in case:
        if c % 2 == 1:
            hap += c
        else:
            pass

    print(f'#{x} {hap}')