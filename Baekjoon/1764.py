# 1764번 듣보잡

# 문제
# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 
# 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.


# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.



# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 
N, M = map(int, input().split())

# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, 
# N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 
dict_ = {}

for _ in range(N):
    name_h = input()
    if name_h not in dict_:
        dict_[name_h] = 1
    else:
        dict_[name_h] += 1

for _ in range(M):
    name_s = input()
    if name_s not in dict_:
        pass
    else:
        dict_[name_s] += 1

for i in range(len(dict_)):
    if dict_[i]


# 입력

# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton

# 출력

# 2
# baesangwook
# ohhenrie