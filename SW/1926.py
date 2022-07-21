# 1926. 간단한 369게임

N = int(input())

for n in range(1, N+1):
    s = str(n)

    cnt = s.count('3') + s.count('6') + s.count('9')

    if cnt == 0:
        print(s, end = ' ')
    else:
        print("-"*cnt, end = ' ')




# N = int(input())
# res = []
# num = []

# for n in range(1, N+1):
#     num.append(n)

# for x in range(1, N+1) :

#     for i in num:

#         for j in range(len(str(i))):  

#             if '3' in str(i) or '6' in str(i) or '9' in str(i):
#                 res.append('-')
#                 # i -= i[j]
#             else:
#                 res.append(i)

# print(*res)



# num = int(input())
# for i in range(1,num+1):
#     i = str(i)
#     clap = i.count('3')+i.count('6')+i.count('9')
#     if clap == 0:
#         print(i, end= " ")
#     else:
#         print("-"*clap, end= " ")



# n=int(input()) # 100
 
# for i in range(1,n+1):
#     cnt = 0
#     s = str(i)
#     for j in s:
         
#         if j == '3' or j == '6' or j == '9':
#             cnt += 1       
             
#     if cnt == 0:
#         print(i,end=' ')
#     else:
#         print("-"*cnt, end=' ',sep='')