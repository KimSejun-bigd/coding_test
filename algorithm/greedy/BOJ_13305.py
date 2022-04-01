# 백준 13305번 : 주유소
n = int(input())

dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

sum_cost = dist[0] * cost[0]
min_cost = cost[0]

i = 1
while i < n-1:
    if min_cost > cost[i]:
        min_cost = cost[i]
    sum_cost += min_cost * dist[i]
    i += 1
print(sum_cost)