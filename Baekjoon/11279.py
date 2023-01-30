# 11279번 최대 힙
# 1927 최소 힙 풀던 것에 이제 - 만 잘 붙여서 넣어주면 됨
# 민우님이 푸셨던거 설명해주셨었음 감품회 최고된다~

import heapq
import sys

heap = []

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    if n != 0:
        heapq.heappush(heap, -n)
        
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))