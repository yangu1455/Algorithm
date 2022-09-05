# 2562번 최댓값

a=[]
for i in range(9):
    a.append(int(input()))
    
x= max(a)
print(x)
y= a.index(x)
print(y+1)