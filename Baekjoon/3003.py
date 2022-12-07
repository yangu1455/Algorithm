# 3003번 킹, 퀸, 룩, 비숍, 나이트, 폰

dong_hyuk = [1, 1, 2, 2, 2, 8]
have = list(map(int, input().split()))

for d in range(len(have)):
    print(dong_hyuk[d]-have[d], end = ' ')