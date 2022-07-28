# 1302번 베스트셀러

# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 
# 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

# 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 
# 이 값은 1,000보다 작거나 같은 자연수이다. 
# 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 
# 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

# 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 
# 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.

N = int(input())
sell_dict = {}

for i in range(N):
    name = input()
    if name not in sell_dict:
        sell_dict[name] = 1
    else:
        sell_dict[name] += 1

max_sell = []

for j in range(len(sell_dict)):
    if len(max_sell) == 0 :
        max_sell.append(max(sell_dict, key = sell_dict.get))
    else:
        
max_sell.sort()
print(max_sell)
