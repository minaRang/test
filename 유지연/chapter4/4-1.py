n = int(input())
x,y=1,1
plans= input().split()
    
dx = [0 ,0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]
#처음에 x,y좌표가 늘어나는게 헷갈렸다 이중배열 좀 더 익숙해지자
#[-1,0] 이렇게 표기안하고 위처럼 표기가 깔끔
        
for plan in plans:
    for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
    if nx<1 or ny < 1 or nx > n or ny > n:
        continue
    x, y= nx, ny
        
print(x,y)