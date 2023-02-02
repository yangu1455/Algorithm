# 11478번 서로 다른 부분 문자열의 개수

S = input()
word = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        # i번째 문자부터 부분 문자열 구해서 word 셋에 넣어주기
        word.add(S[i:j+1])

print(len(word))