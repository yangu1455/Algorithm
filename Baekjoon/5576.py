# 5576번 콘테스트

W_list = []
K_list = []

# 입력은 20 행으로 구성된다. 
for n in range(20):
    score = int(input())

    # 1 번째 줄부터 10 번째 줄에는 W 대학의 각 참가자의 점수를 나타내는 정수가 
    if n < 10:
        W_list.append(score)
    # 11 번째 줄부터 20 번째 줄에는 K 대학의 각 참가자의 점수를 나타내는 정수가 적혀있다. 
    else:
        K_list.append(score)

W_list.sort()
K_list.sort()

# 긴 논의 끝에 참가한 10 명 중 득점이 높은 사람에서 3 명의 점수를 합산하여 대학의 득점으로하기로 했다.
w = W_list[-1] + W_list[-2] + W_list[-3]
k = K_list[-1] + K_list[-2] + K_list[-3]

# W 대학 점수와 K 대학의 점수를 순서대로 공백으로 구분하여 출력하라.
print(w, k)