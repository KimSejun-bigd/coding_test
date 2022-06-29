from queue import PriorityQueue
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = []

    for i in range(len(priorities)):
        queue.append((priorities[i], i))

    while queue:
        max_pri = max(queue)[0]
        tmp = queue.pop(0)

        if tmp[0] < max_pri:
            queue.append(tmp)
        else:
            if location == tmp[1]:
                break
            answer += 1

    return answer+1

if __name__ == '__main__':
    priorities = 	[1, 1, 9, 1, 1, 1]
    location = 	0
    print(solution(priorities, location))