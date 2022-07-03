# 백준 1697번 : 숨바꼭질
import sys
from collections import deque

def bfs():
    if n == k:
        print(0)
        exit(0)
    queue = deque()
    queue.append(n)

    # ex) 1000 0 술래가 뒤에 있을 수 도 있다
    dist = [0] * (max(n, k)) * 2
    while queue:
        x = queue.popleft()
        dx = [-1, 1]
        # 순간이동 현재 * 2
        dx.append(x)

        for i in range(3):
            nx = x + dx[i]
            if nx < 0 or nx >= len(dist):
                continue
            if dist[nx] == 0 or (dist[nx] > dist[x] + 1 and dist[nx] != 0):
                dist[nx] = dist[x] + 1
                queue.append(nx)
    print(dist[k])


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    bfs()