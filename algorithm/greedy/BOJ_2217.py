# 백준 2217번 : 로프
n = int(input())

max = 0
lope = []
for _ in range(n):
    lope.append(int(input()))
lope.sort()

for i in range(n):
    tmp = lope[i] * (n-i)
    if max < tmp:
        max = tmp
print(max)