# 백준 5585번 : 거스름돈
money = 1000 - int(input())

cnt = 0
bal = [500, 100, 50, 10, 5, 1]

while money > 0:
    for i in range(6):
        cnt += money // bal[i]
        money = money % bal[i]
print(cnt)