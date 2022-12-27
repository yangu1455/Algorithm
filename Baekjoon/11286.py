# 11286번 절댓값 힙

# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 
# 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

# 첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 
# 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
# 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
# x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 
# 입력되는 정수는 -231보다 크고, 231보다 작다.

# 입력에서 0이 주어진 회수만큼 답을 출력한다. 
# 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

import heapq
import sys

heap = []

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    if n != 0:
        # heapq.heappush(heap, item) : item을 heap에 추가
        heapq.heappush(heap, (abs(n), n))
        # heap을 tuple로 구성했을 때 맨 앞 숫자만 가지고 정렬하므로 
        # 앞은 abs(절대값) 내장 함수를 써주고 
        # 두 번째는 원래 수를 써줌으로써 절댓값 정렬을 할 수 있게 한다.
        
    else:
        if len(heap) == 0:
            print(0)
        else:
            # [1] 이유!
            print(heapq.heappop(heap)[1])



#==============================
# 우선순위 큐를 이용해보자 1

import heapq as hq
import sys

input = sys.stdin.readline
pq = []

for _ in range(int(input())):
    x = int (input())
    if x :
        hq.heappush(pq, (abs(x), x))
    else:
        print(hq.heappop(pq)[1] if pq else 0)

#===============================
# 우선순위 큐를 이용해보자 2

import heapq as hq
import sys

input = sys.stdin.readline
min_heap = [] # 양수
max_heap = [] # 음수
for _ in range(int(input())):
    x = int(input())
    if x :
        if x > 0:
            hq.heappush(min_heap, x)
        else:
            hq.heappush(max_heap, -x) # 부호를 바꿔서 최대힙
    else:
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(-max_heap[0]):
                    print(hq.heappop(min_heap))
                else:
                    print(-hq.heappop(max_heap))
            else:
                print(hq.heappop(min_heap))
        else:
            if max_heap:
                print(-hq.heappop(max_heap))
            else:
                print(0)