# 1926. 간단한 369게임

N = int(input())
res = []
num = []

for n in range(1, N+1):
    num.append(n)

for x in range(1, N+1) :

    for i in num:

        for j in range(len(str(i))):  

            if '3' in str(i) or '6' in str(i) or '9' in str(i):
                res.append('-')
                # i -= i[j]
            else:
                res.append(i)

print(*res)






# s = ''

# for x in range(1, N+1):
#     s = s + ' ' + str(x)

# s = s.replace('3', '-')
# s = s.replace('6', '-')
# s = s.replace('9', '-')

# res = s.split()
