# deque라이브러리를 사용하는 것이 좋음
# 실제 수행 시간이 DFS보다 좋은 편이다
# 큐이용 & 큐 자료구조 이용

from collections import deque

def  bfs(graph, start, visited):
    queue = deque([start])
    visited[start] =  True
    while queue:
        v = queue.popleft() #가장 먼저들어온 원소 꺼낼 수 있음
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]

visited = [False] * 9
bfs(graph, 1, visited)