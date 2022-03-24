# 백준 2206번 : 벽 부수고 이동하기
import copy
from collections import deque

def bfs():
    queue = deque()
    queue.append((0,0))



n, m = map(int, input().split())

graph = []
wall = set()

for i in range(n):
    tmp = list(map(int,input()))
    graph.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == 1:
            wall.add((i,j))

visited = [[False] * m for _ in range(n)]
answer = 1

for xy in wall:
    bfs()