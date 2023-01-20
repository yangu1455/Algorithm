# 9655번 돌 게임

# 시작하는 사람이 정해져있고, 1개 혹은 3개만 가져갈 수 있다. (2개가 남았을 때 2개만 가져가지 못한다)
# 1일 때는 SK
# 2일 때는 CY
# 3일 때는 다시 SK
# 4일 때는 CY가 이긴다.
 
# 그렇다면 n개가 있을 때는 어떻게 구할까? SK가 이기는 경우의 수를 가정해보자.
# 이는 점화식으로 풀 수 있다. 1개 혹은 3개만 가져갈 수 있으므로 상대방의 선택지는 n-1 혹은 n-3이 될 것이다.
# 따라서 자신이 가져갈 수 있는 다음 경우의 수는 n-2, n-4, n-6 총 3가지가 될 것이다.
# 이렇게 쭉 내려가다 보면 결국 SK는 n이 홀 수 일 때 이길 수 있고, 짝수 일 때는 방법이 없이 CY가 우승을 차지하게 된다.
# 그림 그리면 더 빨리 이해할 수 있다.
# 출처 : https://claude-u.tistory.com/325


N = int(input())

if N % 2 == 0:
    print('SK')
else:
    print('CY')