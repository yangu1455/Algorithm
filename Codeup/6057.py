a, b = map(int, input().split())
c = bool(a)
d = bool(b)
print(((not c) and (not d)) or (c and d))


# 불 값이 서로 같을 때 = not&not or ...&...