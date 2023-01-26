# 2805번 나무 자르기

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
tree_h = list(map(int, sys.stdin.readline().rstrip().split()))
start, end = 0, max(tree_h)

while start <= end:
    mid = (start + end) // 2
    tree = 0 # 잘린 나무 합
    for i in tree_h:
        if i > mid: # mid보다 큰 나무 높이는 잘림
            tree += i - mid

    if tree >= M: # 원하는 나무 높이보다 더 많이 잘렸으면
        start = mid + 1
    else: # 원하는 나무 높이보다 덜 잘렸으면
        end = mid - 1

print(end)