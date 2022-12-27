# 11047번 동전 0

# (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
# 'Ai는 Ai-1의 배수' 라고 적혀있기 때문에 그리디로 풀수가 있다!

import sys

# 첫째 줄에 N과 K가 주어진다. 
N, K = map(int, sys.stdin.readline().split())
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. 
coins = [int(sys.stdin.readline()) for _ in range(N)]
# 최소의 갯수를 만들어야하기 때문에 큰 값의 동전부터 나눠줘야한다.
# 그래서 동전 값이 큰 순서로 한 번 뒤집어준다.
coins.reverse()
ans = 0

for coin in coins:
    ans += K // coin
    K %= coin

# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
print(ans)