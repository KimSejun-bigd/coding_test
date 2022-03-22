# 백준 2468번 : 안전지대
import sys
import copy
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if copy_graph[x][y] ==  0:
        return False
    copy_graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)
    return True

n = int(input())

graph = []
# 방향벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

answer = 0
for h in range(0, 101): # 비가 안 올 수도 있다...
    #deepcopy 안하면 graph의 값이 계속 바뀜
    copy_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            # 높이가 낮은 지점을 0으로 바꿈
            if copy_graph[i][j] <= h:
                copy_graph[i][j] = 0
    result = 0
    for i in range(n):
        for j in range(n):
             if dfs(i,j):
                 result += 1
    answer = max(answer, result)

print(answer)