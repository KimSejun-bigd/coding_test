# 백준 1049번 : 기타줄
import sys
n, m = map(int, input().split())

price = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

res = 0
pack_price = sorted(price, key=lambda x:x[0])[0][0]
per_price = sorted(price, key=lambda x:x[1])[0][1]

# 6개 패키지가 가격 < 낱개 6개 가격
if pack_price < per_price * 6:
    # 낱개로 사야하는 가격 > 6개 패키지 가격이면 패키지 하나 더 사는게 이득
    if pack_price < per_price * (n % 6):
        res = pack_price * (n // 6 + 1)
    else:
        res = pack_price * (n // 6) + per_price * (n % 6)
else:
    res = per_price * n

print(res)