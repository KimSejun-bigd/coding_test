# 백준 7569번 : 토마토(3차원)
from collections import deque

def bfs():


    while queue:
        zz, xx, yy = queue.popleft()
        for i in range(6):
            nx = xx + dx[i]
            ny = yy + dy[i]
            nz = zz + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[zz][xx][yy] + 1
                queue.append((nz, nx, ny))


queue = deque()
m, n, h  = map(int, input().split())


graph = [[] for _ in range(h)]

#방향 벡터
#좌 우 앞 뒤 상, 하
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))


answer = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                # 익은 토마토 위치 큐에 넣기
                queue.append((i, j, k))
bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            answer = max(answer, graph[i][j][k])


print(answer-1)