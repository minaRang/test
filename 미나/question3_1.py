n,m,k=map(int,input().split())
data = list(map(int,input().split())) #배열입력받기

data.sort()#내림차순 정렬
f=data[n-1]#가장 큰 수
s=data[n-2]#두번째로 큰 수
result=0

#가장 큰 수가 더해지는 횟수 m-(m%k)
for i in range(m-(m%k)):
    result+=f
#두번째 수가 더해지는 횟수 m%k
for i in range(m%k):
    result+=s

print(result)