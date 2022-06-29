# 백준 1697번 : 아기상어
from collections import deque
import sys


# 현재 위치에서 물고기들의 거리를 구해주는 함수
def bfs(x, y):
    dist = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    fish_list = []
    queue = deque()
    global baby_size

    space[x][y] = 0
    visited[x][y] = True
    queue.append((x, y))

    while queue:
        pre_x, pre_y = queue.popleft()
        for i in range(4):
            nx = pre_x + dx[i]
            ny = pre_y + dy[i]

            # 범위 밖으로 벗어남
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 처음 방문한 곳 && 아기상어랑 사이즈가 같거나 작은 -> 이동가능
            if not visited[nx][ny] and space[nx][ny] <= baby_size:
                dist[nx][ny] = dist[pre_x][pre_y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

                # 먹을 수 있는 물고기라면
                if 0 < space[nx][ny] < baby_size:
                    fish_list.append((nx, ny, dist[nx][ny]))

    # 현위치에서 먹을 수 있는 가장 가까운(거리가 같다면 가장 위쪽, 왼쪽의) 물고기 선택
    # 먹을 수 있는 물고기가 없으면 (-1, -1, -1) 리턴
    fish_list.sort(key=lambda x: (x[2], x[0], x[1]))
    if len(fish_list) > 0:
        return fish_list[0]
    else:
        return (-1, -1, -1)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    space = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    answer = 0
    eat_cnt = 0
    now_x = now_y = 0
    baby_size = 2
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                now_x, now_y = i, j

    while True:
        xx, yy, d = bfs(now_x, now_y)
        if xx == yy == d == -1:
            break
        eat_cnt += 1
        answer += d
        now_x = xx
        now_y = yy
        if eat_cnt == baby_size:
            eat_cnt = 0
            baby_size += 1
    print(answer)