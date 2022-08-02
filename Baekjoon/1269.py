# 1269번 대칭 차집합


# 자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 
# 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오. 
# 두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.

# 예를 들어, A = { 1, 2, 4 } 이고, B = { 2, 3, 4, 5, 6 } 라고 할 때,  
# A-B = { 1 } 이고, B-A = { 3, 5, 6 } 이므로, 대칭 차집합의 원소의 개수는 1 + 3 = 4개이다.


# 첫째 줄에 대칭 차집합의 원소의 개수를 출력한다.

# import sys
# an, bn = map(int,sys.stdin.readline().split())
# # heapq.heappush(A, (map(int, input().split())))
# A = set(map(int,sys.stdin.readline().split()))
# end = time.time()
# # B = list(map(int,sys.stdin.readline().split()))
# # end = time.time()
# # res_A = [x for x in A if x not in B] # 집합 간의 뺄셈을 구현함(서치함..)
# # res_B = [x for x in B if x not in A]
# # print(len(res_A)+len(res_B))

# print(f"{end - start:.5f} sec")

an, bn = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A-B)+len(B-A))
