n = int(input())
array = list(map(int, input().split()))
d = [0] * 1000 #초기화과정 -> 받은 배열아니라 만든거니까
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])
