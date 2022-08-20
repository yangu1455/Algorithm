# 9020번 골드바흐의 추측

# 짝수가 입력으로 들어오면 그것을 두 소수의 합으로 나타내야한다.
# 만약 여러쌍이 나오는 경우 그 두 소수의 차가 가장 적은 것으로 표현한다.


# 소수인지 판별하는 함수
def isPrime(a):
    if a == 1 :
        return False
    else : 
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0 :
                return False
        return True

# 테스트 케이스 수
T = int(input())

for _ in range(T):
    # 짝수 입력받기
    n = int(input())
    a, b = n//2, n//2
    while a > 0:
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1