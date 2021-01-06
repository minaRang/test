#다시 풀어보기, 잘 이해가지 x
#이번 알고리즘 기말 증명
#적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾기
#이 과정에서 이중 for문
n,m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)
d[0] = 0 #0이 이처럼 가능하므로 불가능한 값을 10001이라 지정함
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]]+1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])