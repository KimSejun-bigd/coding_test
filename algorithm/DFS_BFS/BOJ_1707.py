# 백준 1707번 : 이분 그래프
from collections import deque
def bfs(start):
    rb = 1 # 그룹을 표현할 값 1, -1 로 인접한 노드 같은지 판단할거
    queue = deque()
    queue.append(start)
    visited[start] = rb
    global flag

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            # 한번도 방문 안한 노드일떄만
            if visited[i] == 0:
                queue.append(i)
                # 이전노드 값에 -1 곱한다
                visited[i] = visited[a] *(-1)
            # 방문했던 노드인데 현재 노드랑 같은 그룹이면 이분 그래프가 아님 바로 리턴
            elif visited[i] == visited[a]:
                flag = True
                return


k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    flag = False

    # 비인접 노드가 있을지 모르니 모든 정점에 대해 탐색
    for i in range(1, v+1):
        # 한번도 탐색 안된 노드에 대해서만
        if visited[i] == 0:
            bfs(i)
        if flag :
            break
    if flag:
        print("NO")
    else:
        print("YES")