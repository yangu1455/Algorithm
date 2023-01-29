# 17219번 비밀번호 찾기

import sys

input = sys.stdin.readline

# 첫째 줄에 저장된 사이트 주소의 수 N(1 ≤ N ≤ 100,000)과 
# 비밀번호를 찾으려는 사이트 주소의 수 M(1 ≤ M ≤ 100,000)이 주어진다.
N, M = map(int, input().rstrip().split())

memo = {}
for _ in range(N):
    # 두번째 줄부터 N개의 줄에 걸쳐 각 줄에 사이트 주소와 비밀번호가 공백으로 구분되어 주어진다. 
    address, password = input().rstrip().split()
    memo[address] = password

add_list = []
for _ in range(M):
    add_list.append(input().rstrip())

for i in add_list:
    print(memo[i])

