# 백준 1202번 : 보석 도둑
# 일반 리스트로 푸니까 시간초과가 남 -> 우선순위 큐를 이용해 푼다 nlogn
# + input으로 받으니까 시간초과 난다...

import heapq
import sys

n, k = map(int, input().split())

jew = []
bag = []
# 보석 정보 초기화
for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    jew.append((m,v))

# 가방 정보 초기화
for _ in range(k):
    bag.append(int(sys.stdin.readline()))

jew.sort()
bag.sort()
heap = []

price = 0
for i in range(len(bag)):
    while jew and bag[i] >= jew[0][0]:
        heapq.heappush(heap, -jew[0][1]) # heaq는 최소힙만 지원하므로 -붙여서 최대힙으로
        heapq.heappop(jew)
    if heap:
        price += heapq.heappop(heap)
print(-price)