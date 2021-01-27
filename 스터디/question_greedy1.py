N=int(input())
fears=list(map(int,input().split()))
fears.sort()
group=0
member=0
for fear in fears:
    member+=1
    if member>=fear:
        group+=1
        member=0

print(group)