# 1620번 나는야 포켓몬 마스터 이다솜
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=lee95292&logNo=221201880034
# isalpha, isdigit 함수

import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

book = {}
for i in range(1, N+1):
    name = input().rstrip()
    book[i] = name
    book[name] = i

for j in range(M):
    q = input().rstrip()
    # q라는 문자열이 숫자인지 아닌지를 판단!
    if q.isdigit():
        print(book[int(q)])
    else:
        print(book[q])