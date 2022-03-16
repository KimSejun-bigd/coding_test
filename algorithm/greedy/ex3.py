#이코테2021 (유투브 동빈나)
# 모험가 길드

N = int(input())
player = list(map(int, input().split()))
#가장 공포도가 낮은 모험가 부터 그룹 만들면 됨
player = sorted(player)

count = 0
result = 0

for i in player:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(count)
