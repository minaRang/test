
n,m=map(int,input().split())
card=[]
result=0

for i in range(n):
    card.append(list(map(int, input().split())))
    if result<min(card[i]):
        result=min(card[i])

print(result)
