# 백준 1012번 : 유기농 배추
import sys
# 백준서버에서 최대 재귀 값은 1000이라 이대로 올리면 에러남
sys.setrecursionlimit(10**6)

def dfs(x,y):
    # 땅 범위를 넘어가면 False
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    # 현재 위치에 배추가 있으면 없다고 처리하고, 상하좌우에 대해 다시 탐색
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

t = int(input())

#테스트 케이스 갯수만큼
for i in range(t):
    n, m, k = map(int, input().split())
    graph = [[0] * m  for _ in range(n)]

    # 배추의 위치 초기화
    for j in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    result = 0
    for k in range(n):
        for l in range(m):
            if dfs(k,l):
                result += 1
    print(result)
