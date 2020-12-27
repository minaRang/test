n,m,k = map(int,input().split())
num = list(map(int,input().split()))
total=0
count=0

m1 = max(num) #가장 큰 수
num.remove(m1)
m2=max(num) #두 번째로 큰 수
num.remove(m2)

while True:
    for j in range(k):
        total+=m1
        count+=1

        if count >= m:
            break

        if j == k - 1:
            total += m2
            count += 1

    if count >= m:
        break

print("가장 큰 수 : ",total)


