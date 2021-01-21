#숫자 입력받고 왼쪽자릿수, 오른쪽 자릿수 저장할 변수 sum, sum1

n=input()
sum=0
sum1=0

#배열 길이 이분할, 양쪽 sum값 비교
for i in range(len(n)//2):
    sum += int(n[i])

for j in range(len(n)//2,len(n)):
    sum1 += int(n[j])

if sum==sum1:
    print("LUCKY")
else:
    print("READY")

