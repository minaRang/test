#럭키 스트레이트
N=input()
l=len(N)
sum1,sum2=0,0
for i in range(l):
    if i<(l/2):
        sum1+=int(N[i])
    else:
        sum2+=int(N[i])
if sum1==sum2:
    print("LUCKY")
else:
    print("READY")
