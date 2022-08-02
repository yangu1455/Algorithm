# 2902번 KMP는 왜 KMP일까?

# 하루는 이 메모를 보던 중, 지금까지 긴 형태와 짧은 형태를 섞어서 적어 놓은 것을 발견했다.
# 긴 형태의 알고리즘 이름이 주어졌을 때, 
# 이를 짧은 형태로 바꾸어 출력하는 프로그램을 작성하시오.

# 입력은 한 줄로 이루어져 있고, 첫 번째 글자는 항상 대문자이다. 
# 그리고, 하이픈 뒤에는 반드시 대문자이다. 그 외의 모든 문자는 모두 소문자이다.

memo = input()
# Knuth-Morris-Pratt
res = ''

for i in range(len(memo)):
    # 첫번째 글자는 무조건 대문자니까 result 리스트에 넣고
    if i == 0:
        res += memo[0]
    # - 를 만나면 - 다음 글자를 result 리스트에 넣는다.
    elif memo[i] == '-':
        res += memo[i+1]

print(res)
# # KMP

# # 오늘 배운 자료구조를 사용해서 풀어보고 싶었는데 도저히 떠오르지 않아서
# # 문자열로만 구현...

# 이건 다른 조원분 풀이
# 대박 간단해서 가지고 왔다.

a = list(input().split('-'))

for i in a:
    print(i[0], end = '')