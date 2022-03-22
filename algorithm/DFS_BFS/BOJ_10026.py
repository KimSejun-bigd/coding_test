# 백준 10026번 : 적록색약
import sys
import copy
sys.setrecursionlimit(10**6)

def dfs(x, y, color, g):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if g[x][y] == '0':
        return False

    # 탐색한 지점은 '0'으로 방문처리
    g[x][y] = '0'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        # 다음 탐색할 위치가 현재의 색깔 문자와 같으면 dfs
        if g[nx][ny] == color:
            dfs(nx, ny, g[nx][ny], g)
    return True


n = int(input())

graph = [] # 적록색약 X
graph_jeokrok = [] # 적록색약

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(input()))

graph_jeokrok = copy.deepcopy(graph)

# 적록색약이 보는 그래프 R->G로 다 바꿔버림
for i in range(n):
    for j in range(n):
        if graph_jeokrok[i][j] == 'R':
            graph_jeokrok[i][j] = 'G'

answer = 0
answer_jeokrok = 0
for i in range(n):
    for j in range(n):
        # 적록색약 아닌사람
        if dfs(i,j, graph[i][j], graph):
            answer += 1
        # 적록색약
        if dfs(i,j, graph_jeokrok[i][j], graph_jeokrok):
            answer_jeokrok += 1

print(answer, answer_jeokrok)