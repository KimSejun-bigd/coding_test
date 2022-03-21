# 백준 1697번 : 숨바꼭질
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        # 현재 위치
        x = queue.popleft()
        #좌우로 걸을때
        dx = [-1, 1]
        # 순간이동(현재위치*2)
        dx.append(x)
        for i in range(3):
            nx = x + dx[i]
            if nx < 0 or nx >= len(graph):
                continue
            if graph[nx] == 0 or (graph[nx] > graph[x] + 1 and graph[nx] != 0):
                graph[nx] = graph[x] + 1
                queue.append(nx)
    print(graph[k])

n, k = map(int, input().split())

if n == k :
    print(0)
    exit(0)

# 술래가 더 뒤에 있을 수도 있다 ex) 1000 0
graph = [0] * (2*max(k, n))

bfs(n)
