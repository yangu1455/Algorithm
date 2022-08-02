# 9012번 괄호

# a = int(input())
# for i in range(a):
#     b = input()
#     s = list(b)
#     sum = 0
    
#     for i in s:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0:
#             print('NO')
#             break
    
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')


# =========================


from collections import deque

T = int(input())

for t in range(T):
    stack = deque()
    Paren = input() # Parenthesis 괄호의 줄임말
    
    for p in Paren:

        if p == '(':
            stack.append(p)
        elif p == ')':
            
            if stack: # 스택이 비어있지 않은 경우
                stack.popleft()
            else: # 스택이 비어있을 경우
                print("NO")
                break
   
    else: # break 되지 않았을 경우
        
        if not stack: # 스택이 비어있다면
            print("YES")
        else: # 스택에 괄호가 남아있다면
            print("NO")


# 놀라운 사실 리스트로 푸는게 더 빠르다...