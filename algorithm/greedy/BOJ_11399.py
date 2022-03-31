# 백준 11399번 : ATM
n = int(input())

time = sorted(list(map(int, input().split())))
ans = 0

for i in range(1, n+1):
    ans += sum(time[0:i])

print(ans)