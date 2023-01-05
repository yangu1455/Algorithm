# 1259번 팰린드롬수

while True:
    num = list(input())
    if num == ['0']:
        break
    else:
        for i in range(len(num)):
            if num[i] == num[len(num)-i-1]:
                res = 'yes'
            else:
                res = 'no'
                break
        print(res)