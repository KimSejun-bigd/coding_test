# 백준 1987번 : 알파벳
# dfs에 인자로 cnt 안주고 visited.count(True)로 했는데 이러면 시간초과가 난다.... O(n)이라서 그런가

def dfs(x, y, cnt):
    global answer
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if visited[ord(graph[nx][ny])-65]:
            continue
        # 알파벳 방문처리
        visited[ord(graph[nx][ny])-65] = True
        dfs(nx, ny,cnt+1)
        # dfs 들여보내고 다른경로에서도 이 알파벳 갈 수 있게 false 처리
        visited[ord(graph[nx][ny])-65] = False
    answer = max(answer, cnt)

    return


r, c = map(int, input().split())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(r):
    graph.append(list(input()))
# 알파벳 방문 여부 리스트
visited = [False] * 26
answer = 1

visited[ord(graph[0][0])-65] = True
dfs(0,0,1)
print(answer)