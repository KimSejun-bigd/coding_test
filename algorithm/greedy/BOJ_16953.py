# 백준 16953번 : A -> B
a, b = map(int, input().split())

if a == b:
    print(1)
    exit(0)

cnt = 0
while b >= a:
    # 2로 나누어떨어지면 나누기2
    if b % 2 == 0:
        b = b // 2
        cnt += 1
    # 홀수인데 끝자리가 1이면 마지막 1떼버림
    elif str(b)[-1] == '1':
        b = b // 10
        cnt += 1
    # 위 두개 조건이 아니라면 만들 수가 없다
    else:
        print(-1)
        exit(0)
    if b == a:
        break
else:
    print(-1)
    exit(0)
print(cnt+1)