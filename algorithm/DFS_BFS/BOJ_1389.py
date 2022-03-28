# 백준 1389번 : 케빈 베이컨의 6단계 법칙
from collections import deque

def bfs(start):
    visited = [0] * (n + 1)
    queue = deque()
    queue.append(start)

    #시작점 1로 방문 판단 나중에 -1 * 유저수 해야함
    visited[start] = 1

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] != 0:
                continue
            visited[i] = visited[a]+1
            queue.append(i)
    list_kevin.append(sum(visited) - n)


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
list_kevin = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

for i in range(1, n+1):
    bfs(i)
print(list_kevin.index(min(list_kevin))+1)