# 1936. 1대1 가위바위보
# 1 가위 2 바위 3 보

A, B = map(int, input().split())

if A == 1:
    if B == 2:
        print('B')   #(1, 2)
    elif B == 3:
        print('A')   #(1, 3)
elif A == 2:
    if B == 1:
        print('A')   #(2, 1)
    elif B == 3:
        print('B')   #(2, 3)
elif A == 3:
    if B == 1:
        print('B')   #(3, 1)
    elif B == 2:
        print('A')   #(3, 2)
