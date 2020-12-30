n,m=map(int,input().split())
a,b,d=map(int,input().split())
da=[0,-1,0,1]
db=[-1,0,1,0]
maps=[]
count=1

#육지인지 바다인지 입력받음 (육지는 0, 바다는 1)
for _ in range(n):
    maps.append(list(map(int,input().split())))
#현재 위치 방문 상태로 초기화
maps[a][b]=1

for i in range(4):
        # 캐릭터의 방향(북동남서)에 따라 왼쪽 검사
        for j in range(4):
            if d==j:
                #갈 수 있는 칸(육지, 방문X)는 0으로 처리, 갈 수 없는 칸(바다, 방문O)은 1로 처리함. 갈 수 있을 경우 이동한다.
                if (maps[a+da[j]][b+db[j]]==0):
                        a+=da[j]
                        b+=db[j]
                        maps[a][b] = 1
                        count+=1
                        i = 0
                #갈 수 없는 경우(바다, 방문O)도 회전은 수행
                d = (d+3)%4

print("방문한 칸의 수 : ", count)
