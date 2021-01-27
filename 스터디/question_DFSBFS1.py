#특정 거리의 도시 찾기
from collections import deque
N,M,K,X = map(int, input().split())
visited = [False] * (n + 1)
path = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    path[a].append(b)
answer = []
q = deque()
q.append((x, 0))
while q:
    town, distance = q.popleft()
    if distance == K:
        answer.append(town)
    elif distance < K:
        for node in path[town]:
            if not visited[node]:
                visited[node] = True
                q.append((node, distance + 1))
 
if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)