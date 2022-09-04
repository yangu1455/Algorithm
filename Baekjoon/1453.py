# 1453번 피시방 알바

import sys

N = int(sys.stdin.readline())
g_list = list(map(int, sys.stdin.readline().split()))
count = 0
g_set = []

for g in range(len(g_list)):
    if g_list[g] not in g_set:
        g_set.append(g_list[g])
    else:
        count += 1

print(count)