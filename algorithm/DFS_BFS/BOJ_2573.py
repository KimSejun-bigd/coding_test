# 백준 2573번 : 빙산
import copy
import sys
from collections import deque


def bfs(x, y):
    global bfs_iceburg
    queue = deque()
    queue.append((x, y))
    bfs_iceburg[x][y] = 0

    while queue:
        o_x, o_y = queue.popleft()
        for i in range(4):
            nx = o_x + dx[i]
            ny = o_y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if bfs_iceburg[nx][ny] != 0:
                queue.append((nx, ny))
                bfs_iceburg[nx][ny] = 0


n, m = map(int, sys.stdin.readline().split())

iceburg = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

while True:
    cnt = 0
    bfs_iceburg = copy.deepcopy(iceburg)

    # 빙산의 덩어리 갯수 체크
    for i in range(n):
        for j in range(m):
            if bfs_iceburg[i][j] != 0:
                bfs(i, j)
                cnt += 1
            if cnt >= 2:
                print(answer)
                exit(0)
    if cnt == 0:
        print(0)
        exit(0)

    # 한 번에 빙산 전부가 녹는 것을 위해 deepcopy
    tmp_iceburg = copy.deepcopy(iceburg)

    # 빙산 주위 바닷물 체크해서 빙산 녹이는 부분
    for i in range(n):
        for j in range(m):
            tmp = iceburg[i][j]
            # 빙하인 경우에는 상하좌우에 바닷물이 있는지 확인
            if tmp != 0:
                water_cnt = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if ni < 0 or nj < 0 or ni >= n or nj >= m:
                        continue
                    if iceburg[ni][nj] == 0:
                        water_cnt += 1

                tmp_iceburg[i][j] = tmp - water_cnt
                if tmp_iceburg[i][j] < 0:
                    tmp_iceburg[i][j] = 0

    iceburg = tmp_iceburg
    answer += 1
