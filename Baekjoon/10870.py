# 10870번 피보나치 수 5

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

a = int(input())
print(fibonacci(a))