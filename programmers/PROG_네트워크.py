def solution(n, computers):
    answer = 0
    global visited
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            # print(i)

    return answer

def dfs(node):
    if visited[node]:
       return
    #방문처리
    visited[node] = True

    for i in range(len(computers[node])):
        if computers[node][i] == 1 and not visited[i]:
            dfs(i)
    return

if __name__ == '__main__':
    n = 3
    computers = 	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    visited = [False] * n
    print(solution(n, computers))