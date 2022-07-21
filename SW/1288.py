# 1288. 새로운 불면증 치료법

T = int(input())

for x in range(T): # 테스트 케이스 만큼 돌려
    N = int(input())
    s = ''
    count = 1

    while True:
        num = str(N * count) # num은 N 곱하기 숫자 1부터~ 2N
        a = list(num) # 이걸 쪼개는거지  0, 2, 5, 9

        for j in a: # 쪼갠거 리스트로 바꿨으니까 하나씩 꺼내서
            if j not in s : # 이게 0123456789 중에 있으면
                s += j

        if len(s) == 10:
            print(f'#{x+1} {num}')
            break

        count += 1
        





# T = int(input())
# s = ''

# for x in range(1, T+1): # 테스트 케이스 만큼 돌려
#     N = int(input())
#     count = 1

#     while len(s) <= 10:
#     # for i in range(1, N+1): # 숫자 1부터 N까지
#         num = str(N * count) # num은 N 곱하기 숫자 1부터~ 2N
#         a = list(num) # 이걸 쪼개는거지  0, 2, 5, 9

#         for j in a: # 쪼갠거 리스트로 바꿨으니까 하나씩 꺼내서
#             if j not in s : # 이게 0123456789 중에 있으면
#                 s += j

#         count += 1

#     print(f'#{x} {count-1}')