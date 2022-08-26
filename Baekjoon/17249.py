# 17249번 태보태보 총난타

# 얼굴의 왼편에 왼손의 잔상이, 오른편에는 오른손이 잔상이 남을 때 혜정이는 주먹을 몇 번 뻗었을까?

# 주먹의 잔상은 =로 시작하여 @로 끝나고, 잔상이 남지 않는 경우는 없다. 얼굴 형태가 (^0^) 꼴이고, 주먹의 잔상이 같은 곳에 위치하지 않는다.

# 입력
# 문자열의 길이는 1,000을 넘지 않는다.

# 출력
# 첫째 줄에 왼손의 잔상의 수와 오른손의 잔상의 수를 출력한다.


left_h = 0
right_h = 0

taebo = input()
cnt = 0

for t in taebo:
    if t == '@':
        cnt += 1
    elif t == '(':
        left_h = cnt
        cnt = 0
right_h = cnt

print(left_h, right_h)