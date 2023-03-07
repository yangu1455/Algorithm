# 15953번 상금 헌터
# https://www.acmicpc.net/problem/15953

# 첫 번째 줄에 제이지가 상상력을 발휘하여 가정한 횟수 T(1 ≤ T ≤ 1,000)가 주어진다.
T = int(input())

# 다음 T개 줄에는 한 줄에 하나씩 제이지가 해본 가정에 대한 정보가 주어진다. 
for i in range(T):
    # 각 줄에는 두 개의 음이 아닌 정수 a(0 ≤ a ≤ 100)와 b(0 ≤ b ≤ 64)가 공백 하나를 사이로 두고 주어진다.
    a, b = map(int, input().split())
    dollar = 0  # 상금 합계, 매 케이스마다 처음에 초기화 시켜줌

    if a == 1:
        dollar += 5000000
    elif 1 < a <= 3:
        dollar += 3000000
    elif 3 < a <= 6:
        dollar += 2000000
    elif 6 < a <= 10:
        dollar += 500000
    elif 10 < a <= 15:
        dollar += 300000
    elif 15 < a <= 21:
        dollar += 100000
    # 진출하지 못하거나 상금받는 등수 이하일 경우
    else:
        pass

    if b == 1 :
        dollar += 5120000
    elif 1 < b <= 3:
        dollar += 2560000
    elif 3 < b <= 7:
        dollar += 1280000
    elif 7 < b <= 15:
        dollar += 640000
    elif 15 < b <= 31:
        dollar += 320000
    else:
        pass

    print(dollar)   # 출력