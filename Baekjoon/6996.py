# 6996번 애너그램

T = int(input())

for t in range(T):
    A, B = input().split()
    x = list(A)
    y = list(B)

    # print(A, type(A))

    for i in A:
        if i in y:
            y.remove(i)
            x.remove(i)

    if len(y) == 0 and len(x) == 0:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')