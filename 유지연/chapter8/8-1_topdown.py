#경우의 수를 생각하면서 탑다운으로 먼저 접근했음 -> 저장해놓고 최솟값 비교
#백준 1463번과 유사
#점화식 끝에 1 더하는게 함수 호출 횟수 구하기 때문 -> 놓쳤음

#탑다운
x = int(input())
d = [0]*30001

def f(x):
    
    if(x == 1): 
        return 0
    if(d[x]!=0): 
        return d[x]

    result = f(x-1) + 1 #1뺀거랑 저장해놓고 나눈거중에 작은 수 비교
    if (x%5==0):
        result = min(result, f(x//5)+1) # 나누기(/)로 하면 소수 나와서 오류생김
    if (x%3==0):
        result = min(result, f(x//3)+1)
    if (x%2==0):
        result = min(result, f(x//2)+1)
    d[x]=result
    
    return d[x]

print(f(x))
#d[x] 전역 변수 아니라 출력해도 값 안나옴 0나옴
