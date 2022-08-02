# 14720번 우유축제

# 0(딸기) -> 1(초코) -> 2(바나나) -> 0(딸기)

# 각각의 우유 가게는 딸기, 초코, 바나나 중 한 종류의 우유만을 취급한다.
# 각각의 우유 가게 앞에서, 영학이는 우유를 사마시거나, 사마시지 않는다.
# 우유거리에는 사람이 많기 때문에 한 번 지나친 우유 가게에는 다시 갈 수 없다.
# 영학이가 마실 수 있는 우유의 최대 개수를 구하여라.

# 0, 1, 2 외의 정수는 주어지지 않는다.

# 영학이가 마실 수 있는 우유의 최대 개수를 출력하시오.

# 우유 가게의 수 N
N = int(input())
# 우유 가게 정보가 N개의 정수로 주어짐
milk_list = list(map(int, input().split()))
# 임의의 변수
number = 0

for m in range(N):
    # m번째 우유 가게가 number라는 임의의 수를 3으로 나눈 나머지(0 or 1 or 2)와 비교
    # 0으로 정의했기때문에 0부터 나온다.
    if milk_list[m] == (number % 3):
        # 그럼 0부터 시작해서 1씩 커진다.
        number += 1

print(number)
        