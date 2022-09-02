# 10871번 X보다 작은 수

n, x= map(int, input().split())

a = list(input().split())

for i in range(1, n+1):
    if int(a[i-1])< x:
        print(a[i-1])