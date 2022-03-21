# 백준 11724번 : 연결 요소의 개수
# python3로 제출하니까 시관초과 난다.... pypy3로 하면 정답이고... python3랑 pypy3(반복 작업이 많을 때 유리) 적절하게 선택해서 사용하자!!
from collections import deque

def bfs(start,visited):
    if visited[start]: return
    queue = deque()
    queue.append(start)
    visited[start] = True
    global result

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    result += 1
    return


n, m = map(int, input().split())

graph = [[]  for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(1, len(visited)):
    if not visited[i]:
        bfs(i, visited)

print(result)