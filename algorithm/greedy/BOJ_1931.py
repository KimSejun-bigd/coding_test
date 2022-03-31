# 백준 1931번 : 회의실 배정
n = int(input())

time = []
for _ in range(n):
    time.append(list(map(int,input().split())))

#회의 끝나는시간이 빠른 순서대로, 같으면 시작시간이 빠른순으로 정렬
time.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = time[0][1]
for i in range(1, n):
    #다음 회의의 시작시간이 끝나는 시간보다 크거나 같을때만
    if end <= time[i][0]:
        cnt += 1
        end = time[i][1]
print(cnt)