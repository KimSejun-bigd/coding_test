# 백준 24479번 : 알고리즘 수업 - 깊이 우선 탐색 1
import sys
sys.setrecursionlimit(10**6)


def dfs(graph, visited, r):
    global cnt
    visited[r] = True
    answer_list[r-1] = cnt
    cnt += 1
    for i in graph[r]:
        if not visited[i]:
            dfs(graph, visited, i)
    return


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

dfs(graph, visited,  r)

print(*answer_list, sep='\n')