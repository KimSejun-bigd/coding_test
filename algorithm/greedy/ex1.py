#이코테2021 (유투브 동빈나)

# 그리디 알고리즘(탐욕법)은 현재 상황에서 지금 당장 좋은것만 고르는 방법을 의미
# 문제를 풀기 위한 최소한의 아이이어를 떠올려야함
# -> 단순히 좋아보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지...

# 예시 : 거스름 돈 문제 -> 가장 큰 화폐단위부터 돈을 거슬러주면 됨

n = 1260
count = 0

array = [500, 100, 50, 10]

#시간 복잡도 O(N) : N은 화폐의 종류 -> 동전의 종류에만 영향을 받음
for coin in array:
    count += n // coin
    n %= coin

print(count)

