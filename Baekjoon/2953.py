# 2953번 나는 요리사다

list0 = {}

for i in range(1, 6):
    score = list(map(int, input().split()))
    hap = sum(score)
    list0[i] = hap
    
k = max(list0, key=list0.get)
v = max(list0.values())
print(f'{k} {v}')