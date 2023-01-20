# 9658번 돌 게임 4
# 돌 게임 3과 모든 조건이 동일하지만, 
# 마지막 돌을 가져간 사람이 지게 되기 때문에 if문의 결과만 바꿔주면 된다!가 아니라 머리를 더 굴려야함
# 3번이랑 비슷하다고 생각해서 그냥 4번째까지 똑같은 리스트를 넣어줬는데
# 절대 그래선 안된다 이전과 분명히 결과가 다르다!!! (4번째가 True)
# 경우 예시를 꼭 들어보기

N = int(input())
# 0개, 1~4개까지는 결과 정하고 나머지(N에서 앞의 4칸을 제외한)는 0으로 채워두기
total = [0, False, True, False, True] + [0] * (N-4)
 
for i in range(5, N+1):
    if False in [total[i-1],total[i-3],total[i-4]]:
        total[i]= True
    else:
        total[i]= False
 
if total[N]:
    print("SK")
else:
    print("CY")