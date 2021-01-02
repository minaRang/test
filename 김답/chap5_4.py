#n,k,a,b의 값을 입력받음
n,k=map(int,input().split())
a=(list(map(int,input().split())))
b=(list(map(int,input().split())))

#a 오름차순, b 내림차순 정렬
a.sort()
b.sort(reverse=True)

#a값이 b값보다 작을 때 값 교환, a값이 b값보다 클 경우 멈춤
for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break

#합을 구하고 출력
sum=0
for i in a:
    sum+=i
print(sum)