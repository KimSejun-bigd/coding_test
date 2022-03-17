#이코테2021 (유투브 동빈나)
# 왕실의 나이트

#방향벡터
drow = [-2, -2, -1, 1, -1, 1, 2, 2]
dcol = [-1, 1, -2, -2, 2, 2, -1, 1]

input_data = input()
row = int(input_data[1])
col = ord(input_data[0]) - ord('a') + 1

count = 0
for i in range(8):
    mrow = drow[i] + row
    mcol = dcol[i] + col
    if mrow <1 or mcol < 1 or mrow > 8 or mcol > 8:
        continue
    count += 1
print(count)