# 2920번 음계

# 1부터 8까지 차례대로 연주한다면 ascending, 
# 8부터 1까지 차례대로 연주한다면 descending, 
# 둘 다 아니라면 mixed 이다.
# 연주한 순서가 주어졌을 때, 
# 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.


# 입력
# 첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.


# 출력
# 첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.



num_list = list(map(int, input().split()))

for n in range(len(num_list)-1):
    if n == len(num_list):
        break
    if abs(num_list[n] - num_list[n+1]) == 1:
        pass
    else:
        print('mixed')
        exit()

if num_list[0] == 1:
    print('ascending')
elif num_list[0] == 8:
    print('descending')


# 사기 코드

# if num_list == [1, 2, 3, 4, 5, 6, 7, 8]:
#     print('ascending')
# elif num_list == [8, 7, 6, 5, 4, 3, 2, 1]:
#     print('descending')
# else:
#     print('mixed')
    