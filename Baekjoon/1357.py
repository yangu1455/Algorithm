# 1357번 뒤집힌 덧셈

def Rev(x):
    reverse_num = ''
    for i in x:
        reverse_num = i + reverse_num
    
    return int(reverse_num)

# 첫째 줄에 수 X와 Y가 주어진다.
X, Y = input().split()
print(Rev(str(Rev(X) + Rev(Y))))