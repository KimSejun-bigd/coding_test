#이코테2021 (유투브 동빈나)
# 시각

#하루는 24*60*60 = 86400 초 이기때문에 완전탐색(Brute Forcing) 가능
#파이썬은 1초에 2천만번의 연산 가능하다고 생각
N = int(input())

count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1
print(count)