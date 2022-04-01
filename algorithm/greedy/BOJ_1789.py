# 백준 1789번 : 수들의 합
s = int(input())

ans = 1

while True:
    if ans * (ans+1) / 2 > s:
        break
    ans += 1
print(ans-1)