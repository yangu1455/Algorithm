# 9325번 얼마?

import sys

# 첫째 줄에 테스트 케이스의 개수가 주어진다.
T = int(sys.stdin.readline())

for t in range(T):
    # 각 테스트 케이스의 첫 줄엔 자동차의 가격 s가 주어진다.    
    s = int(sys.stdin.readline())
    # 둘째 줄엔 해빈이가 구매하려고 하는 서로 다른 옵션의 개수 n이 주어진다.
    n = int(sys.stdin.readline())

    # 옵션을 계산한 가격 리스트에 담아 저장!
    opt_list = []
    # 뒤이어 n개의 줄이 입력으로 들어온다. 
    for _ in range(n):
    # 각 줄은 q 와 p로 이루어져 있는데 q는 해빈이가 사려고 하는 특정 옵션의 개수이고 p는 해당 옵션의 가격이다.
        q, p = map(int, sys.stdin.readline().split())
        opt_list.append(q * p)
    
    for i in opt_list:
        s += i

    print(s)