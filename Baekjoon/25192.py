# 25192번 인사성 밝은 곰곰이

# 받을 데이터의 수
N = int(input())
# 곰곰인사하는 사람을 넣을겁니다!
count = set()
# enter 할때마다 count 되는 사람 수를 전부 합할겁니다!
res = 0

for _ in range(N):
    # 입장을 나타내는 ENTER, 혹은 채팅을 입력한 유저의 닉네임이 문자열로 주어진다.
    sta = input()

    # ENTER를 만나면
    if sta == 'ENTER':
        # 기존에 set에 모여있던 사람들의 수를 결과 값에 저장하고 set을 초기화 시킨다.
        res += len(count)
        count.clear()
    else:
        # 유저의 닉네임이 들어오면 set에 값을 저장한다.
        count.add(sta)

# for문이 끝나면 count에 들어있던 유저의 수를 세서 결과 값에 더해준다.
res += len(count)
print(res)