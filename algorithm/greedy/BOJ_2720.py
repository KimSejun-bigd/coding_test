# 백준 2720번 : 세탁소 사장 동혁
t = int(input())
coin = [25, 10, 5, 1]

for _ in range(t):
    c = int(input())
    while c > 0:
        for i in coin:
            cnt = c // i
            c %= i
            print(cnt, end=' ')
    print()

