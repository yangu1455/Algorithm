a, b, c = map(int, input().split())
d = (a if a<b else b) if ((a if a<b else b)<c) else c
print(d)

# a, b, c = map(int, input().split())
# print(min(a, b, c))

# (a if a>b else b) if ((a if a>b else b)>c) else c --> 가장 큰 값 계산하기