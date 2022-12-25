# 5800번 성적 통계

import sys

# 첫째 줄에 중덕 고등학교에 있는 반의 수 K가 주어진다. 
K = int(sys.stdin.readline())

for k in range(1, K+1):
    # 다음 K개 줄에는 각 반의 학생수 N과 각 학생의 수학 성적이 주어진다. 
    g_list = list(map(int, sys.stdin.readline().split()))
    N = g_list[0]
    g_list.remove(g_list[0])
    g_list.sort(reverse = True)  # 내림차순 정렬하는~
    max_gap = 0

    for g in range(len(g_list)-1):
        if g_list[g] - g_list[g+1] > max_gap:
            max_gap = g_list[g] - g_list[g+1]

    print(f'Class {k}')
    print(f'Max {g_list[0]}, Min {g_list[-1]}, Largest gap {max_gap}')