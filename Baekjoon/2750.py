# 2750번 수 정렬하기

N = int(input())
num = []

for _ in range(N) : 
    num.append(int(input()))

num.sort()

for i in num:
    print(i)