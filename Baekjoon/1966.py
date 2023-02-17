# 1966번 프린터 큐
# https://www.acmicpc.net/problem/1966
# https://assaeunji.github.io/python/2020-05-04-bj1966/

# 출력
# 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

import sys

input = sys.stdin.readline

# 첫 줄에 테스트케이스의 수가 주어진다.
T = int(input())

for _ in range(T):
    # 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 
    # 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 
    N, M = map(int, input().split())
    import_list = list(map(int, input().split()))
    index_list = list(range(N))
    # 인덱스 리스트도 순서가 계속 바뀔 것이기 때문에 처음부터 문자열이든 뭐든으로 바꿔서 크게 표시해둔다.
    index_list[M] = 'HERE'

    cnt = 0

    # for문으로 절대 돌리면 안돼...
    # 한바퀴만 돌고 끝이 아니라 값이 맞아 떨어질때까지 계속 돌아야하기 때문!
    while True:
        # 중요도 리스트의 첫 항목이 최댓값이면
        if import_list[0] == max(import_list): 
            # 인쇄 시작을 위해 cnt += 1 
            cnt += 1 
            # 인덱스 리스트 첫 항목이 찾고 있는 것이라면!
            if index_list[0] == 'HERE':
                print(cnt)
                break
            # 아니라면 아무값도 필요없으니까 그냥 먼저 인쇄하고 값은 날려버림
            else:
                import_list.pop(0)
                index_list.pop(0)

        # 아닌 경우에는
        else:
            import_list.append(import_list.pop(0))
            index_list.append(index_list.pop(0))


# 입력
# 3 테스트케이스 수
# 1 0 문서의 개수, 찾고있는 문서가 현재 queue에서 몇번째에 놓여있는지(인덱스)
# 5 케이스 1 문서의 중요도
# 4 2
# 1 2 3 4 케이스 2 문서의 중요도
# 6 0
# 1 1 9 1 1 1 케이스 3 문서의 중요도

# 출력
# 1
# 2
# 5
