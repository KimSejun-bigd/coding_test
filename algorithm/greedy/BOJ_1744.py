# 백준 1744번 : 수 묶기
import sys
n = int(sys.stdin.readline())
res = 0

list_plus = []
list_minus = []
list_one = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 1:
        list_one.append(num)
    elif num > 0:
        list_plus.append(num)
    else:
        list_minus.append(num)

list_plus.sort(reverse=True)
list_minus.sort()
list_one.sort(reverse=True)

print(res)