# end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
# 기본적으로 end 다음에 \n가 들어있는 상태임
# sep은 print하나만 쓰고 여러 개행으로 나눌 수 있음
# 스택이용 & 재귀함수 이용

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 그래프 문제에서 노드 1부터 시작하는 경우 많이때문에 0번째 비워두고자 []
# 각 노드에 인접한 노드 리스트    
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
# 인덱스 0 사용하지 않기위해 하나 더 큰 9개 사용

dfs(graph, 1, visited)