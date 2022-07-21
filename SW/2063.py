# 2063. 중간값 찾기

N = int(input())

list0 = sorted(map(int, input().split()))
l = round(len(list0) // 2)

print(list0[l])