n,k =map(int,input().split())
count=0

while n!=1:
    while True:
        if (n%k)==0:
            break
        else:
            n-=1
            count+=1

    while True:
        if (n%k)!=0:
            break
        else:
            n/=k
            count += 1

print("1이 될 때까지 최소 횟수 : ",count)