# 1874번 스택 수열

# 스택 (stack)은 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
# 이를 계산하는 프로그램을 작성하라.

# 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 
# 물론 같은 정수가 두 번 나오는 일은 없다.

# 출력
# 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. 
# push연산은 +로, pop 연산은 -로 표현하도록 한다.
# 불가능한 경우 NO를 출력한다.


# https://velog.io/@ny_/%EB%B0%B1%EC%A4%80-1874%EB%B2%88.-%EC%8A%A4%ED%83%9D-%EC%88%98%EC%97%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://pacific-ocean.tistory.com/231
# https://hongcoding.tistory.com/39

import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    num = int(input())



# 입력
# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1


# 출력
# +
# +
# +
# +
# -
# -
# +
# +
# -
# +
# +
# -
# -
# -
# -
# -


n = int(input())
stack = []
answer = []
flag = 0
cur = 1 # 1이상 n이하의 정수
for i in range(n):
    num = int(input())
    while cur <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append("+")
        cur += 1
    # 입력한 수를 만나면 while문 탈출. 즉 cur = num일 때 까지 while문을 돌아 스택을 쌓는다.

    if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면
        stack.pop()         # 스택의 TOP을 꺼내 수열을 만들어 준다.
        answer.append("-")
    else:                   # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        print("NO")         # 왜냐하면 12345 처럼 오름차순으로 스택이 입력되는데
        flag = 1            # TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
        break               # exit()하고 flag 안써도 되긴함

if flag == 0:
    for i in answer:
        print(i)