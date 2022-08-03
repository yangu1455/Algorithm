# 5533번 유니크

# 각 플레이어는 1이상 100 이하의 정수를 카드에 적어 제출한다. 
# 각 플레이어는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻는다. 
# 만약, 같은 수를 쓴 다른 사람이 있는 경우에는 점수를 얻을 수 없다.

# 각 플레이어가 각각 쓴 수가 주어졌을 때, 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 참가자의 수 N이 주어진다.
N = int(input())
# 둘째 줄부터 N개 줄에는 각 플레이어가 1번째, 2번째, 3번째 게임에서 쓴 수가 공백으로 구분되어 주어진다.
# matrix = [list(map(int, input().split())) for _ in range(N)]
# [[100, 99, 98], [100, 97, 92], [63, 89, 63], [99, 99, 99], [89, 97, 98]]
# 위처럼 받는 것보다 게임 별로 받는게 훨씬 쉬울 것 같다!
first_g = []
second_g = []
third_g = []

for i in range(N):
    a, b, c = map(int, input().split())
    first_g.append(a)
    second_g.append(b)
    third_g.append(c)

for j in range(N):
    score = 0

    if first_g.count(first_g[j]) == 1:
        score += first_g[j]
    if second_g.count(second_g[j]) == 1:
        score += second_g[j]
    if third_g.count(third_g[j]) == 1:
        score += third_g[j]

    print(score)

# 각 플레이어가 3번의 게임에서 얻은 총 점수를 입력으로 주어진 순서대로 출력한다.
# for num in range(N):
#     print(sum(matrix[num]))