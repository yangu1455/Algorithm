# 10814번 나이순 정렬

N = int(input())
list_ = []

for _ in range(1, N+1):
    age, name = input().split()
    list_.append((int(age), name))

list_.sort(key = lambda x : x[0])  # (age, name)에서 age만 비교

# 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.
for i in list_ :
    print(i[0], i[1])

# 이중에서 정렬하기
# 람다 함수 https://wikidocs.net/64
# 2중 리스트에서 정렬하기 https://infinitt.tistory.com/122