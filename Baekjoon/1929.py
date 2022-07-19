import sys

m, n = map(int, sys.stdin.readline().split())
res = []

def isPrime(a): # 에라토스테네스의 체
    if a == 1 :
        return False
    else : 
        for i in range(2, int(a ** 0.5) + 1): # 범위를 제곱근까지만으로 줄여
            if a % i == 0 :
                return False
        return True

for j in range(m, n+1):
    if isPrime(j):
        print(j)



# num_count = int(input())
# num_list = list(map(int, input().split(' ')))
# d = 0
 
# if len(num_list) == num_count:   
#     for i in num_list:     
#         count = 0        
#         for j in range(1,i+1):     
#             if i % j == 0:   
#                 count += 1
#         if count == 2:   
#             d += 1
# print(d)



# import time
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")