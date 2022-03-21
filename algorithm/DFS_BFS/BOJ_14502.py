# 백준 14502번 : 연구소
# 조합을 이용해서 벽을 세울 수 있는 경우의 수를 다 돌려서 답은 맞았는데... 이게 맞는건가...
from itertools import combinations
import copy

def dfs(x, y):
    # 바이러스 걸린 구역일 때만 상하좌우 본다
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 넘어가면 넘어감
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 벽 말고 빈공간일때만 전파
        if temp_graph[nx][ny] == 0:
            temp_graph[nx][ny] = 2
            dfs(nx, ny)
    return


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# n >= 3, m >= 8 최대 사각형 크기 24
# 대충 24에서 벽 위치 3개 뽑는 경우의 수 24P3 -> 2024 밖에 안됨. 브루트 포스 해도 될듯

wall = 0
list_empty = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            list_empty.append((i, j))

# 빈 공간에 벽을 세울 수 있는 경우의 수 전부
list_wall_combi = list(combinations(list_empty, 3))

safe = 0
for i in list_wall_combi:
    # deepcopy 안쓰면 graph의 값이 계속 바뀐다
    temp_graph = copy.deepcopy(graph)
    for j in i:
        # 벽 세움
        temp_graph[j[0]][j[1]] = 1
    for j in range(n):
        for k in range(m):
            if temp_graph[j][k] == 2:
                # 바이러스 있는 위치에서 dfs 돌림
                dfs(j, k)
    tmp_safe = 0
    for i in temp_graph:
        for j in i:
            if j == 0:
                tmp_safe += 1
    if safe < tmp_safe:
        safe = tmp_safe
print(safe)

