# 백준 1260번 : DFS와 BFS
from collections import deque

def dfs(graph, start, visited):
    #현재노드 방문처리
    visited[start] = True
    print(start, end= ' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque()
    #큐에 현재노드 삽임
    queue.append(start)
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

n, m, v = map(int, input().split())

graph = [[] * _ for _ in range (n+1)]

#그래프 초기화
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#작은 정점순으로 정렬
for i in graph:
    i.sort()

visited = [False] * (n+1)
dfs(graph, v, visited)
visited = [False] * (n+1)
print()
bfs(graph, v, visited)
#print("".join(graph))