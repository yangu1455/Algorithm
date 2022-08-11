# 2979번 트럭 주차

# 첫째 줄에 문제에서 설명한 주차 요금 A, B, C가 주어진다.
A, B, C = map(int, input().split())
# 주차된 시간을 리스트에 기록함
# 입력으로 주어지는 시간은 1과 100사이 이다.
time_list = [0] * 101

# 다음 세 개 줄에는 두 정수가 주어진다. 
for _ in range(3):
    # 이 정수는 상근이가 가지고 있는 트럭이 주차장에 도착한 시간과 주차장에서 떠난 시간이다. 
    x, y = map(int, input().split())
    
    for i in range(x, y):
        time_list[i] += 1

# 첫째 줄에 상근이가 내야하는 주차 요금을 출력한다.
# 트럭을 한 대 주차할 때는 1분에 한 대당 A원을 내야 한다. 
# 두 대를 주차할 때는 1분에 한 대당 B원, 세 대를 주차할 때는 1분에 한 대당 C원을 내야 한다.
print(time_list.count(1) * A + time_list.count(2) * 2 * B + time_list.count(3) * 3 * C)