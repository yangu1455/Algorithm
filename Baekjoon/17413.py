# 17413번 단어 뒤집기 2
# 풀이 참고 https://hongcoding.tistory.com/62  => 많이 다르긴함..ㅎ

# 띄어쓰기가 있으면 거꾸로
# 괄호 안에 들어있으면 그대로 출력해야함

# 만날수 있는 경우의 수
# 공백을 만난다
# 괄호를 만난다
# 아무것도 만나지 않고 끝난다

import sys

input = sys.stdin.readline

S = input().rstrip()

i = 0
# 괄호가 밖의 문자열
string = ''
# 결과
res = ''

while i < len(S):
    # 들어온 문자가 괄호 시작인 경우
    if S[i] == '<':
        if string:
            res += string[::-1]
            string = ''
        res += '<'
        i += 1
        while S[i] != '>':
            res += S[i]
            i += 1
    elif S[i] == '>':
        res += '>'
        i += 1
    # 괄호 밖
    else:
        # 공백이 아닐 경우
        if S[i] != ' ':
            string += S[i]
            i += 1
        # 공백이 온 경우
        else:
            # 뒤집힌 단어들을 결과에 넣고
            res += string[::-1]
            # 그 뒤에 공백을 붙여준다
            res += ' '
            string = ''
            i += 1

if string:
    res += string[::-1]

print(''.join(res))