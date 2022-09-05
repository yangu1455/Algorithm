# 2577번 숫자의 개수

A= int(input())
B= int(input())
C= int(input())
x= list(str(A*B*C))

for i in range(10):
    print(x.count(str(i)))