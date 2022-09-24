# 1302번 베스트셀러

# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 
# 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

# 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 
N = int(input())
# 제목을 키로 받고 값에 1씩 더해주기
sell_dict = {}

# 둘째부터 N개의 줄에 

for _ in range(N):
    # 책의 제목이 입력으로 들어온다. 
    name = input()
    if name not in sell_dict:
        sell_dict[name] = 1
    else:
        sell_dict[name] += 1

# sell_dict {'name' : 1, ... }

# 제일 많이 판 책의 개수
max_sell = max(sell_dict.values())
# 최종 적으로 나와야하는 책의 제목 리스트
res_list = []

for k, v in sell_dict.items():
    if v == max_sell:
        # max(딕셔너리 이름, 키 = 딕셔너리이름.get) 하면 딕셔너리에서 가장 큰 밸류의 키 값을 불러올 수 있다.
        res_list.append(k)

# 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.
res_list.sort()
# 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 
print(res_list[0])


# # 입력

# 5
# top
# top
# top
# top
# kimtop


# # 출력

# top