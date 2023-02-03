# 10815번 숫자 카드

import sys

input = sys.stdin.readline

# 상근이가 가지고 있는 숫자 카드의 개수
N = int(input().rstrip())
# 상근이의 숫자카드에 적혀있는 정수
sang = set(input().rstrip().split())
# 확인해볼 정수의 갯수
M = int(input().rstrip())
# 확인해볼 정수들
check = list(input().rstrip().split())

res_list = []
for num in check:
    if num in sang:
        res_list.append(1)
    else:
        res_list.append(0)

for i in res_list:
    print(i, end=' ')