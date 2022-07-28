# 2058. 자릿수 더하기

N = input()
sum_ = 0

for i in range(len(N)):
    sum_ += int(N[i])

print(sum_)