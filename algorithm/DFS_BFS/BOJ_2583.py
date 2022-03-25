# 백준 2583번 : 영역 구하기
from collections import deque

def bfs(x, y):
    if graph[x][y] == 1:
        return False
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1
    sum = 1

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = 1
                sum += 1
    width.append(sum)
    return True


m, n, k = map(int , input().split())
graph = [[0] * n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

cnt = 0
width = []
for i in range(m):
    for j in range(n):
        if bfs(i,j):
            cnt += 1
print(cnt)
for i in sorted(width):
    print(i, end = ' ')