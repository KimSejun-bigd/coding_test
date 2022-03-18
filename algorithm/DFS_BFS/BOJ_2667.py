# 백준 2667번 : 단지번호붙이기
def dfs(x, y):
    global cnt
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

count = 0 # 단지 수
h_count = [] # 단지에 속하는 집의 수를 담을 리스트
cnt = 0 # 단지에 속하는 집의 수
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            count += 1
            h_count.append(cnt)
            cnt = 0
print(count)
h_count.sort()
for i in h_count:
    print(i)