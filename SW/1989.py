# 1989. 초심자의 회문 검사

T = int(input())

for x in range(1, T+1):
    res = 0
    s = input()
    for i in range(len(s)):
        if s[i] == s[len(s)-i-1]:
            res = 1
        else :
            res = 0
            break
    
    print(f'#{x} {res}')