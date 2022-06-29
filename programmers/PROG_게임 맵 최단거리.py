from collections import deque

def solution(maps):
    dist = [ [-1] * len(maps[0]) for _ in range(len(maps)) ]
    answer = bfs(maps, dist)

    return answer

def bfs(maps, dist):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0,0))
    dist[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            #맵 밖으로 벗어난 경우
            if nx >= len(maps) or nx < 0 or ny >= len(maps[0]) or ny < 0:
                continue
            #맵에서 갈 수 없는 곳
            if maps[nx][ny] == 0:
                continue
            #한번도 방문 안한 곳
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
            #이미 방문한 곳은 최단거리 체크
            else:
                dist[nx][ny] = min(dist[x][y]+1 ,dist[nx][ny])

    return dist[len(maps)-1][len(maps[0])-1]

if __name__ == '__main__':
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    print(solution(maps))