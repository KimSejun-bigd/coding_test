# 백준 1946번 : 신입사원
t = int(input())

for _ in range(t):
    n = int(input())
    score = []
    for i in range(n):
        score.append(list(map(int, input().split())))
    # 우선 서류성적 순으로 나열
    score.sort()
    # 서류 1등의 인터뷰성적 최저성적으로 놓음
    min_interview = score[0][1]
    ans = 1
    for i in score:
        # 서류순으로 정렬을 했으니까, 인터뷰 성적이 내 위에 있는 사람보다 높아야 뽑힌다
        if min_interview > i[1]:
            min_interview = i[1]
            ans += 1
    print(ans)