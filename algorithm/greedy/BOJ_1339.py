# 백준 1339번 : 단어수학
n = int(input())
alpha = [0] * 26

word = []
for _ in range(n):
    word.append(list(input()))

for i in range(len(word)):
    for j in range(len(word[i])):
        # 알파벳의 위치대로 1을 대입해서 alpha 리스트에 넣어둔다
        alpha[ord(word[i][j]) - 65] += 10 ** (len(word[i])-j-1)
# 내림차순으로 정렬을 하면 비중이 큰 순서대로 정렬된다. 그 후에 9부터 곱해주고 더하자
alpha.sort(reverse=True)

num = 9
ans = 0
for i in alpha:
    ans += i * num
    num -= 1

print(ans)