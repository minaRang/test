#나중에 다시 풀어보기! 빠트린 조건이 많았다
# 방향 도는거 다시 돌아나오기 등등

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x,y,direction = map(int, input().split())
d[x][y] = 1
# 북 0 동 1 남 2 서 3

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북 동 남 서 북(-1,0) 동(0,1) 남(1,0) 서(0,-1) 행/열
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3 #돌았을때 연결 -1, 3 연결위해

count = 1
turn_time = 0 #동서남북 다 돌아보는 제한 위해
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 후 가보지 않은 칸 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다
    else:
        turn_time += 1
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

    
print(count)
