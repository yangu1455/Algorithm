# 1986번 지그재그 숫자

N = int(input())

for h in range(1, N+1) :
    t = int(input())
    res = 0
    for i in range(1, t+1) :
        if i % 2 == 0 :
            i = -i
            res += i
        else :
            res += i

    print(f'#{h} {res}')