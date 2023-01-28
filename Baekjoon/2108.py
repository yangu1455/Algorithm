# 2108번 통계학

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
list_ = []

for i in range(N):
    list_.append(int(input()))

list_.sort()

print(round(sum(list_)/N))
print(list_[N//2])

# 최빈수는 풀이 참고함
# https://somjang.tistory.com/entry/BaekJoon-2108%EB%B2%88-%ED%86%B5%EA%B3%84%ED%95%99-Python
cnt = Counter(list_).most_common(2)

if len(list_) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(abs(max(list_) - min(list_)))