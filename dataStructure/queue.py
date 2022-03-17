# 큐
# 먼저 들어온 데이터가 먼저 나가는 형식(FIFO)

# 리스트로도 구현이 가능하지만 시간복잡도가 더 높아서 비효율적으로 동작할 수 있음
# 꼭 deque 라이브러리 사용!!
from _collections import deque
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 순서대로 출력