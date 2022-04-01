# 백준 10610번 : 30
n = list(input())
n.sort(reverse=True)

ans = 0
# 모든 자리의 숫자 합이 3의 배수가 아니거나 0이 없으면 30의 배수가 될 수 없다
if sum(map(int,n)) % 3 != 0 or '0' not in n:
    ans = -1
# 위의 조건을 만족하고 내림차순으로 정렬한 가장 첫번째 숫자가 가장 큰 숫자
else:
    ans = int(''.join(n))

print(ans)