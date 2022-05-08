# 백준 1449번 : 수리공 항승
n, l = map(int, input().split())

location = list(map(int, input().split()))
location.sort()

avail_tape = l - 1
res = 0

if n == 1:
    print(1)
    exit(0)

start = 0
end = 1

while True:
    a = location[start]
    b = location[end]
    if b - a <= avail_tape:
        end += 1
    else:
        res += 1
        start = end
        end += 1
    if end >= n:
        break

print(res + 1)