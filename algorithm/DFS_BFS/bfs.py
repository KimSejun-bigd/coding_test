# BFS(Breadth-First Search)
# 너비 우선 탐색, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
# BFS는 큐 자료구조를 이용
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리함
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
# ==> 특정 조건에서의 최단경로 구하는 문제에서 잘 쓰임

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    #현재노드 방문처리
    visited[start] = True

    #큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end = ' ')
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [], # 문제에서 노드의 번호가 1번부터 시작하는 경우가 많아서 0을 비워둠
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 9 # 노드 0번 사용하지 않기 위해 8보다 하나 더 크게

# bfs 함수 호출
bfs(graph, 1, visited)