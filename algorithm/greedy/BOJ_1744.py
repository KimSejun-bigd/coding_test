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

# 양수계산
# 양수 짝수개이면 다 곱해서 더하고 아니면 가장 작은거 하나 빼고 곱해서 더함
if len(list_plus) % 2 == 0:
    for i in range(0, len(list_plus), 2):
        res += list_plus[i] * list_plus[i+1]
else:
    res += list_plus[-1]
    for i in range(0, len(list_plus)-1, 2):
        res += list_plus[i] * list_plus[i+1]

# 음수, 0 계산
# 음수 짝수개이면 다 곱해서 더하고 아니면 가장 작은거 하나 빼고 곱해서 더함
if len(list_minus) % 2 == 0:
    for i in range(0, len(list_minus), 2):
        res += list_minus[i] * list_minus[i+1]
else:
    res += list_minus[-1]
    for i in range(0, len(list_minus)-1, 2):
        res += list_minus[i] * list_minus[i+1]

# 1 계산
# 전부 더함
res += len(list_one)

print(res)