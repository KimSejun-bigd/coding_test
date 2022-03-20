# 백준 7576번 : 토마토
from collections import deque

def bfs(graph):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


m, n = map(int, input().split())
graph = []
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            # 익은 토마토가 있는 위치 큐에 넣음 (시작위치)
            queue.append((i, j))

bfs(graph)

result = 0
# 그래프 돌려서 안익은 토마토 있는지 확인 + 최대값(토마토 다 익힐 때 까지의 일 수) 구하기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        result = max(result, graph[i][j])

# 시작을 1일부터 했으니 -1
print(result-1)