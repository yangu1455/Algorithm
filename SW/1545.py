T = int(input())
res = []

for test_case in range(T + 1):
	res.append(test_case)

res.reverse()
print(*res)