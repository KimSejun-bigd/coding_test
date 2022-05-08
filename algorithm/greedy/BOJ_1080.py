# 백준 1080번 : 행렬
import sys

def transMatrix(x, y):
    if x + 3 > n or y + 3 > m:
        return
    global cnt
    for i in range(x, x+3):
        for j in range(y, y+3):
            if mat_A[i][j] == 1:
                mat_A[i][j] = 0
            else:
                mat_A[i][j] = 1
    cnt += 1


n, m = map(int, sys.stdin.readline().split())

mat_A = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
mat_B = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if mat_A[i][j] != mat_B[i][j]:
            transMatrix(i, j)


for i in range(n):
    for j in range(m):
        if mat_A[i][j] != mat_B[i][j]:
            print(-1)
            exit(0)
print(cnt)