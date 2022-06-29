def solution(n, costs):
    answer = 0
    #부모 노드 초기화
    parent = [0] * n
    for i in range(n):
        parent[i] = i

    #크루스칼 알고리즘을 위해 비용으로 오름차순 정렬
    costs.sort(key=lambda x:x[2])

    for cost in costs:
        s, e, c = cost[0], cost[1], cost[2]
        #두 노드의 부모 노드가 서로 다르면 싸이클 X -> union
        if find_parent(parent, s) != find_parent(parent, e):
            #신장트리에 간선 추가
            union_parent(parent, s, e)
            answer += c

    return answer

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


if __name__ == '__main__':
    n = 5
    costs = 	[[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]
    print(solution(n, costs))