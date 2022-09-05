# 2231번 분해합

n = int(input())
res = 0

for i in range(1, n+1):        
    a = list(map(int, str(i)))  
    l = i + sum(a)              
    if(l == n):                 
        res = i                   
        break

print(res)