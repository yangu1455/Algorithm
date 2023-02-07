# 9375번 패션왕 신해빈

import sys

# 테스트 케이스
T = int(sys.stdin.readline())

for i in range(T):
    # 해빈이가 가진 의상 수
    n = int(sys.stdin.readline())
    clothes = {}
    for j in range(n):
        # 다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다.
        c = list(sys.stdin.readline().rstrip().split())

        # 의상 종류가 딕셔너리 안에 이미 들어있는 경우
        if c[1] in clothes:
            # 의상 이름을 하나 추가시켜준다.
            clothes[c[1]].append(c[0])
        else:
            # 들어있지 않은 경우 이름과 종류 넣어준다.
            clothes[c[1]]=[c[0]]

    cnt = 1 # 각 종류마다 항목의 개수

    # 경우의 수 구하기
    for k in clothes:
        # 안 입는 경우도 포함해서 길이 구한 것에 더해주기 and 곱하기
        cnt *= (len(clothes[k])+1)
    # 온통 알몸인 경우 제외
    print(cnt-1)