# 백준 24444번 : 알고리즘 수업 - 너비 우선 탐색 1
import sys
from collections import deque


def bfs(graph, visited, r):
    queue = deque()
    global cnt
    queue.append(r)
    visited[r] = True
    answer_list[r-1] = cnt
    cnt += 1

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                answer_list[i-1] = cnt
                cnt += 1


n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
answer_list = [0] * n
cnt = 1

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
    graph[i].sort()

bfs(graph, visited,  r)

print(*answer_list, sep='\n')