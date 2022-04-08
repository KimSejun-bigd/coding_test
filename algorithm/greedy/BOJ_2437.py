# 백준 2437번 : 저울
n = int(input())

num = list(map(int,input().split()))
num.sort()

res = 0
for i in num:
    if res + 1 >= i:
        res += i
    else:
        break
print(res + 1)