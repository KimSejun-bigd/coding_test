#이코테2021 (유투브 동빈나)
# 곱하기 혹은 더하기

s = input()
result = int(s[0])

for i in range(1, len(s)):
    #두 수 중 하나라도 0 or 1이면 더하기
    num = int(s[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
