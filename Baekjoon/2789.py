# 2789번 유학 금지


# 이메일의 각 단어 중에서 CAMBRIDGE에 포함된 알파벳은 모두 지우기로 했다. 
# 즉, 어떤 이메일에 LOVA란 단어가 있다면, A는 CAMBRIDGE에 포함된 알파벳이기 때문에, 
# 받아보는 사람은 LOV로 받는다.
# 이렇게, 어떤 단어가 주어졌을 때, 검열을 거친 후에는 어떤 단어가 되는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 이 단어는 적어도 3글자이며, 많아야 100글자이다.


# 출력
# 입력으로 주어진 단어를 정부가 검열을 하면 어떻게 변하는지를 출력한다. 
# 즉, 단어에서 CAMBRIDGE에 포함된 알파벳을 모두 지운 뒤 출력한다. 항상 정답의 길이는 0보다 크다.

word_ = input()

for w in word_:
    if w in 'CAMBRIDGE':
        word_ = word_.replace(w, '')

print(word_)