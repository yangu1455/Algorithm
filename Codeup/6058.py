a, b = map(int, input().split())
c = bool(a)
d = bool(b)
print(((not c) and (not d)) or not(c or d))


# 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.