# 10866번 덱

import sys

N = int(sys.stdin.readline().strip())
deq = []

for i in range(N):
    com = sys.stdin.readline().strip()

    if 'push_back' in com:
        deq.append(int(com[10:]))

    elif 'push_front' in com:
        deq.insert(0, int(com[11:]))

    elif com == 'size':
        print(len(deq))

    elif com == 'empty':
        if len(deq) != 0:
            print(0)
        else:
            print(1)

    elif com == 'pop_front':
        if len(deq) != 0:
            print(deq[0])
            deq.pop(0)
        else:
            print(-1)

    elif com == 'pop_back':
        if len(deq) != 0:
            print(deq[-1])
            deq.pop(-1)
        else:
            print(-1)
    elif com == 'front':
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)
    elif com == 'back':
        if len(deq) != 0:
            print(deq[-1])
        else:
            print(-1)


# 15
# push_back 1
# push_front 2
# front
# back
# size
# empty
# pop_front
# pop_back
# pop_front
# size
# empty
# pop_back
# push_front 3
# empty
# front



# 2
# 1
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