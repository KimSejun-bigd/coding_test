def solution(n):
    answer = []

    # 가로, 세로 변수 초기화
    h = -1
    w = 0
    num = 1

    #달팽이 초기화
    for i in range(1, n+1):
        tmp = [0 for _ in range(i)]
        answer.append(tmp)

    for i in range(n):
        for j in range(i, n):
            #아래로 내려감
            if i % 3 == 0:
                h += 1
            #오른쪽으로감
            elif i % 3 == 1:
                w += 1
            #위로 올라감
            else:
                h -= 1
                w -= 1
            answer[h][w] = num
            num += 1

    return sum(answer, [])

if __name__ == '__main__':
    n = 3
    print(solution(n))
