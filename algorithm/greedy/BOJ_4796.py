# 백준 4796번 : 캠핑
i = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    cnt = 0
    if v % p > l:
        cnt = v // p * l + l
    else:
        cnt = v // p * l + v % p

    print("Case %d: %d"  %(i, cnt))
    i += 1