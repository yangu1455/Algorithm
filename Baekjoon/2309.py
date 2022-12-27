# 2309번 일곱 난쟁이

# 난쟁이들의 키를 받아서 리스트로 만든다!
list_ = [int(input()) for _ in range(9)]
# 리스트에 들어있는 키를 전부 합한다!
total = sum(list_)

for i in range(9):
    # j는 i 다음 숫자!
    for j in range(i+1,9):
        
        # 리스트에 들어있는 전체 값의 합에서 요소 두개를 뺐을 때 100이 될 경우
        if total - (list_[i] + list_[j]) == 100: 
            
            # 해당 요소를 n1, n2라고 하고
            n1, n2 = list_[i], list_[j]
            
            # 리스트에서 해당 요소를 제거한다.
            list_.remove(n1)
            list_.remove(n2)
            
            # 일곱 난쟁이의 키를 오름차순으로 출력해야한다.
            list_.sort()

            for i in list_:
               print(i)
            exit()


#=====================================
# 조합(combination)을 이용해서 푸는 방법

from itertools import combinations

heights = [int(input()) for _ in range(9)]
for combi in combinations(heights, 7):
    if sum(combi) == 100:
        for height in sorted(combi):
            print(height)
        break