# 백준 2606번 : 바이러스
from collections import deque


def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    virus = []
    while queue:
        x = queue.popleft()
        virus.append(x)
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    # virus 리스트에 탐색된 노드(컴퓨터) 넣어두고 자기자신 뺀 갯수 출력
    print(len(virus)-1)


v = int(input())
n = int(input())

graph = [[] * _ for _ in range(v+1)]
# 방문판별 리스트
visited = [False] * (v+1)
# 그래프 초기화
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1번 컴퓨터부터 bfs 돌리면 인접한 노드를 다 탐색함
bfs(graph, 1, visited)
