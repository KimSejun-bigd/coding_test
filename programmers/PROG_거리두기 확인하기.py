from collections import deque

def bfs(graph, x, y, dist):
    queue = deque()


def solution(places):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in places:
        tmp_list = []
        tmp_dist = 0
        for j in i:
            tmp_list.append(list(j))

        for t_i in range(5):
            for t_j in range(5):
                if tmp_list[t_i][t_j] == 'P':
                    bfs(tmp_list, t_i, t_j, 0)

    answer = []


    return answer

if __name__ == '__main__':
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))