# 백준 2644번 : 촌수계산
from collections import deque

def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[a] + 1

n = int(input())

start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range (n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(start)
print(visited[end]-1 if visited[end] != 0 else -1)