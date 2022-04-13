# 백준 2847번 : 게임을 만든 동준이
t = int(input())

score = [int(input()) for _ in range(t)]
score.reverse()

pre_score = score[0]
res = 0
for i in range(1, t):
    if score[i] >= pre_score:
        res += score[i] - pre_score + 1
        pre_score = pre_score - 1
    else:
        pre_score = score[i]

print(res)