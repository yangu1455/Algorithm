# 10845번 큐

import sys

N = int(sys.stdin.readline().strip())
que = []

for i in range(N):
    com = sys.stdin.readline().strip()
    if 'push' in com:
        que.append(int(com[5:]))
    elif com == 'front':
        if len(que) != 0:
            print(que[0])
        else:
            print(-1)
    elif com == 'back':
        if len(que) != 0:
            print(que[-1])
        else:
            print(-1)
    elif com == 'size':
        print(len(que))
    elif com == 'empty':
        if len(que) != 0:
            print(0)
        else:
            print(1)
    elif com == 'pop':
        if len(que) != 0:
            print(que[0])
            que.pop(0)
        else:
            print(-1)