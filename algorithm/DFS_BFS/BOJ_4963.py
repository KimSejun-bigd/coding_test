# 백준 4963번 : 섬의 개수
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]
            dfs(nx, ny)
        return True


# 상 하 좌 우 대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

while True:
    w, h = map(int, input().split())
    if w == h == 0: break

    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j):
                result += 1
    print(result)
