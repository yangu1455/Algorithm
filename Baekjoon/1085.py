# 1085번 직사각형에서 탈출

x, y, w, h = map(int, input().split())
a = w-x
b = h-y

print(min(a, b, x, y))