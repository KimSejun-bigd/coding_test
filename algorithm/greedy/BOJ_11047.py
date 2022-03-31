# 백준 1047번 : 동전 0
n, k = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))
coin = sorted(coin, reverse=True)

cnt = 0

while k > 0:
    for i in coin:
        cnt += k // i
        k %= i
print(cnt)