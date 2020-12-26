n,m=map(int,input().split())
result=0

for i in range(n):
    data = list(map(int, input().split()))
    data.sort()

    #임시변수 temp에 해당 배열 중 가장 작은 수 저장
    temp = data[0]

    #임시변수에 저장된 값과 result를 비교해서, 큰 수 저장
    if temp > result:
        result = temp

print(result)