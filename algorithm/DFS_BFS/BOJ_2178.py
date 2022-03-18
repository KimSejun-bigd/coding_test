# 백준 2178번 : 미로탐색
# 최단거리 -> BFS
from collections import deque


def bfs(graph, start):
    queue = deque()
    # 현재 위치 큐에 삽입
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 상하좌우로 움직인 좌표
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] != 1:
                continue
            # 미로 밖으로 나가지 않거나 처음온 좌표면
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

    print(graph[n - 1][m - 1])


n, m = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

# 방향벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
bfs(maze, (0, 0))
