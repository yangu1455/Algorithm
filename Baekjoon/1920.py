# 1920번 수 찾기

# 시간초과 - 리스트라서 오래걸림 set으로 하면 가뿐해짐 아래처럼 O(N)
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

for i in M_list:
    if i in A:
        print(1)
    else:
        print(0)
    
# =============================================
 
# A를 set으로 만들어 탐색 - 이분탐색보다 빠름 O(1)
N = int(input())
A = set(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

for num in M_list:
    if num in A:
        print(1)
    else:
        print(0)

# =============================================

# 이분탐색법 - 문제가 원한 해결방법 O(log N)
# https://wayhome25.github.io/cs/2017/04/15/cs-16/
# 다른 사람 풀이법 1
# https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-1920%EB%B2%88-%EC%88%98-%EC%B0%BE%EA%B8%B0-Python

# 입력
N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()			# A 정렬

# arr의 각 원소별로 이분탐색
for num in arr:
    lt, rt = 0, N - 1		# lt는 맨 앞, rt는 맨 뒤
    isExist = False		# 찾음 여부

    # 이분탐색 시작
    while lt <= rt:		# lt가 rt보다 커지면 반복문 탈출
        mid = (lt + rt) // 2	# mid는 lt와 rt의 중간값
        if num == A[mid]:	# num(목표값)이 A[mid]값과 같다면 (목표값 존재여부를 알았다면)
            isExist = True	# isExist Ture 변경
            print(1)		# 1 출력
            break		# 반복문 탈출
        elif num > A[mid]:	# A[mid]가 num보다 작으면
            lt = mid + 1	# lt를 높임
        else:			# A[mid]가 num보다 크다면
            rt = mid - 1	# rt를 낮춤

    if not isExist:		# 찾지 못한 경우
        print(0)		# 0 출력



# 다른 사람 풀이법 2
# https://chancoding.tistory.com/44

from sys import stdin, stdout
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l,N,start,end))