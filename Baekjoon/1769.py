# 1769번 3의 배수

import sys

input = sys.stdin.readline

X = list(map(int, input().rstrip()))
cnt = 0  # 문제 변환 과정 카운트

while len(X) > 1: # 한자리 수가 될 때까지 반복문 실행
    cnt += 1  # 문제 변환 과정 카운트 + 1
    sum_X = sum(X)  # 각 자리수 더해준 것

    X = []  # X 리스트 초기화
    for i in str(sum_X):
        X.append(int(i))  # 각 자리수를 다시 리스트에 넣어준다.

# 문제 변환 과정 몇 번 돌렸는지 출력하기
print(cnt)

# 나오게 된 한 자리 수가 3의 배수인지 확인
if X[0] % 3 == 0:
    print("YES")
else:
    print("NO")