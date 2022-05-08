def solution(lottos, win_nums):
    cnt = 0
    answer = []
    for i in range(len(win_nums)):
        if lottos[i]!= 0 and lottos[i] in win_nums:
            cnt += 1
    max_rank = 7-lottos.count(0)-cnt if 7-lottos.count(0)-cnt < 7 else 6
    min_rank = 7-cnt if 7-cnt < 7 else 6
    answer.append(max_rank)
    answer.append(min_rank)   
    return answer

if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))