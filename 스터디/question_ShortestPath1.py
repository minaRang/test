#플로이드
n=int(input())
m=int(input())
bus=[[999999]*(n+1) for _ in range(n+1)]
for i in range(n):
    bus[i][i]=0
for _ in range(m):
    start,goal,cost=map(int,input().split())
    if cost<bus[start][goal]:
        bus[start][goal]=cost 

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            bus[i][j]=min(bus[i][j],bus[i][k]+bus[k][j])

for i in bus[1:]:
    for j in i[1:]:
        print(j,end=' ')
    print('')