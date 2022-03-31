# 백준 10162번 : 전자레인지
t = int(input())

cnt_300 = 0
cnt_60 = 0
cnt_10 = 0
while True:
    flag = False
    if t == 0:
        break
    if t // 300 != 0:
        cnt_300 = t // 300
        t %= 300
        flag = True
    if t // 60 != 0:
        cnt_60 = t // 60
        t %= 60
        flag = True
    if t // 10 != 0:
        cnt_10 = t // 10
        t %= 10
        flag = True
    if not flag:
        print(-1)
        exit(0)

print(cnt_300, cnt_60, cnt_10)