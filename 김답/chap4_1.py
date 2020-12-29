# 공간의 크기 입력, 이동 계획 입력, 현재 좌표 값을 담을 변수 생성
n=int(input("공간의 크기 입력: "))
print("이동 계획 입력: ",end='');plan=list(map(str,input().split()))
m = [1,1]

# 계획을 하나씩 확인하며 공간을 벗어나지 않는 경우 좌표를 변경
for a in plan:
    if a=='L':
        if not((m[1]-1)<1):
            m[1]-=1
    elif a=='R':
        if (m[1]+1)<n:
            m[1]+=1
    elif a == 'U':
        if not ((m[0] - 1) < 1):
            m[0] -= 1
    elif a == 'D':
        if not ((m[0] + 1) > n):
            m[0] += 1

print("도착할 지점의 좌표 : ", m)