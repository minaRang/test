n,k = map(int,input().split())
result=0

if n%k!=0:
    while n%k>0:
        n-=1
        result +=1
if n%k==0:
    while n//k>0:
        result +=1
        n=n//k

print(result)

