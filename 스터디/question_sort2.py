N=int(input())
houses=list(map(int,input().split()))
houses.sort()
minimum=99999
for i in range(houses[0],houses[-1]+1):
    distance=0
    for house in houses:
        distance+=abs(i-house)
    if distance<minimum:
        pos=i
        minimum=distance

print(pos)