# 1157번 단어 공부

words = input().upper()
w = list(set(words))

cnt_list = []

for x in w :
    cnt = words.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))
    print(w[max_index])