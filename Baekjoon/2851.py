# 2851번 슈퍼 마리오

score = 0
score_dict = {}
a = 0
b = 0

for i in range(1, 11): # 10개의 버섯 먹어서 점수의 합을 딕셔너리에 넣기
    s = int(input())
    score += s
    score_dict[i] = score

for j in range(1, len(score_dict)+1) : # 딕셔너리 길이만큼 반복문
    if score_dict[j] > 100:  # 100보다 크거나 같으면 정지해서 해당 인덱스의 값과 그 이전 값을 a, b에 저장
        a = score_dict[j] 
        b = score_dict[j-1]
        break
    elif score_dict[j] == 100:
        a = score_dict[j]

if score_dict[10] > 100 :
    if abs(a - 100) != 0: # 절댓값 함수를 써서 a에서 100을 뺀 수가 100과 같지 않으면 
        # 100을 뺀 절댓값 크기 비교해서 출력
        if abs(a - 100) <= abs(b - 100): 
            print(a)
        elif abs(a - 100) > abs(b - 100): 
            print(b)
    else: # 절댓값이 100이면 a 출력
        print(a)
else :
    print(score)