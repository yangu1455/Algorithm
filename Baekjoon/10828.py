# 10828번 스택

import sys

N = int(sys.stdin.readline().strip())
stac = []

for i in range(N):
    com = sys.stdin.readline().strip()
    if 'push' in com:
        stac.append(int(com[5:]))
    elif com == 'top':
        if len(stac) != 0:
            print(stac[-1])
        else:
            print(-1)
    elif com == 'size':
        print(len(stac))
    elif com == 'empty':
        if len(stac) != 0:
            print(0)
        else:
            print(1)
    elif com == 'pop':
        if len(stac) != 0:
            print(stac[-1])
            stac.pop()
        else:
            print(-1)


# 입력
# 14
# push 1
# push 2
# top
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# top

# 출력
# 2
# 2
# 0
# 2
# 1
# -1
# 0
# 1
# -1
# 0
# 3