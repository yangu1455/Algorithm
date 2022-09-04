# 1152번 단어의 개수

string = map(str, input().split())
cnt = 0

for word in string:
    if word != "":
        cnt += 1

print(cnt)