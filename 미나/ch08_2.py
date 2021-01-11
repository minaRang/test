n=int(input())#정수 n,식량창고의 갯수
array=list(map(int,input().split())) #모든 식량정보

d=[0]*100 #식량갯수 최대 100개

d[0]=array[0]#첫번째 인덱스는 식량정보list의 첫번째 인덱스값 저장
d[1]=max(array[0],array[1])#두번째 인덱스는 식량정보의 첫번째 인덱스와 두번째 인덱스중 더 큰 값

#2부터 식량창고의 갯수-1 만큼 반복
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])

print(d[n-1])
