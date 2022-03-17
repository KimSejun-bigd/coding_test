# 스택
# 박스를 쌓을 때를 떠올리면 됨 -> 나중에 쌓은걸 먼저 뺌
# 후입선출(LIFO)

# 파이썬의 리스트는 스택으로 사용하기 적합 - append(), pop() 시간 복잡도 O(1)
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단(가장 먼저 나가고자 하는 순서)부터 출력
print(stack) # 최하단(가장 나중에 나가고자 하는 순서)부터 출력