# 백준 13549번 : 숨바꼭질3
from collections import deque

def bfs(start):
    if n == k:
        print(0)
        exit(0)
    queue = deque()
    queue.append(start)
    graph[start] = 0

    while queue:
        x = queue.popleft()
        dx = [-1, 1, x]
        for i in range(3):
            nx = x + dx[i]
            if nx >= len(graph) or nx < 0:
                continue
            if i != 2:
                if graph[nx] == -1 or (graph[nx] != -1 and graph[nx] > graph[x] + 1):
                    graph[nx] = graph[x] + 1
                    queue.append(nx)
            else:
                if graph[nx] == -1 or (graph[nx] != -1 and graph[nx] > graph[x]):
                    graph[nx] = graph[x]
                    queue.append(nx)
    print(graph[k])


n, k = map(int, input().split())


# 술래가 더 뒤에 있을 수도 있다 ex) 1000 0
graph = [-1] * (2*max(k, n))

bfs(n)
