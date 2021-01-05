# n x m 문제는 그 칸을 벗어나지 않도록 조건을 설정해주어야한다. 
# 리스트에 map 사용하기 https://dojang.io/mod/page/view.php?id=2286
 
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
        
def dfs(x,y):
    if x<= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] =1
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1
        
print(result)