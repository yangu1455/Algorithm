# 9657번 돌 게임 3
# 풀이 - https://kau-algorithm.tistory.com/306

N = int(input())
# 0개, 1~4개까지는 결과 정하고 나머지(N에서 앞의 4칸을 제외한)는 0으로 채워두기
total = [0, True,False,True,True] + [0]*(N-4)
 
for i in range(5,N+1):
    if False in [total[i-1],total[i-3],total[i-4]]:
        total[i]= True
    else:
        total[i]=False
 
if total[N]:
    print("SK")
else:
    print("CY")

# 입력
# 6
# 출력
# SK