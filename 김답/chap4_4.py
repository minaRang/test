n,m=map(int,input().split())
a,b,d=map(int,input().split())
da=[0,-1,0,1]
db=[-1,0,1,0]
maps=[]
visit_state=[]#방문 여부 확인을 위한 리스트 0은 미방문, 1은 방문
count=1

#육지인지 바다인지 입력받고 (육지는 0, 바다는 1) 방문 여부 모두 0으로 초기화
for _ in range(n):
    maps.append(list(map(int,input().split())))
    visit_state.append([0]*m)
#현재 위치 방문 상태로 초기화
visit_state[a][b]=1

#캐릭터의 움직임이 멈출때까지 방문한 칸의 수를 센다.
for i in range(4):
        # 캐릭터의 방향(북동남서)에 따라 왼쪽 검사
        for j in range(4):
            if d==j:
                #print("현재 위치 :", a,",",b,"/ 방향 :",j,"/ 왼쪽좌표:(",a+da[j],",",b+db[j],"), ",end='')
                #가보지 않은 칸이고 육지면 왼쪽으로 회전하고 방문
                if (maps[a+da[j]][b+db[j]]==0) and (visit_state[a+da[j]][b+db[j]]==0):
                        d = (d+3)%4
                        a+=da[j]
                        b+=db[j]
                        visit_state[a + da[j]][b + db[j]] = 1
                        count+=1
                        i = 0
                #가본 칸이거나 바다면 왼쪽으로 회전만 수행
                else:
                    d = (d+3)%4

print("방문한 칸의 수 : ", count)




