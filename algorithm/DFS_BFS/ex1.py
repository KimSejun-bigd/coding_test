# 이코테2021 (유투브 동빈나)
# 음료수 얼려 먹기

def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if graph[x][y] == 0:
        #현재 노드를 방문처리
        graph[x][y] = 1
        #상하좌우에 대해 재귀적으로 dfs호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

#입력값 N, M 받음
n, m = map(int, input().split())

#2차원 리스트
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 0:미방문, 1:방문으로 처리리
#모 노드에 대해서 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result += 1

print(result)