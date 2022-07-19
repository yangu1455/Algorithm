T = int(input())
res = 0

for test_case in range(1, T + 1):
    a = map(int, input().split())
    hap = 0
    for i in a:
        hap += i
    
    res = round(hap / 10)
    print(f'#{test_case} {res}')


# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1   