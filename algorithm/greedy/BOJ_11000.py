# 백준 11000번 : 강의실 배정
import sys
import heapq

n = int(sys.stdin.readline())

heap = []
res = 0
for _ in range(n):
    s, t = map(int, sys.stdin.readline().split())
    heap.append([s, t])

# 시작시간 순으로 정렬
heap.sort(key=lambda x: x[0])

room = []
heapq.heappush(room, heap[0][1])

for i in range(1, n):
    if heap[i][0] < room[0]:
        heapq.heappush(room, heap[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, heap[i][1])
print(len(room))
