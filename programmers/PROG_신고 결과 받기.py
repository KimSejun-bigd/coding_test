def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list)) ]

    tmp = [ set([]) for _ in range(len(id_list)) ]
    cnt_report = [0 for _ in range(len(id_list)) ]

    # 신고 한 사람 set에다가 저장
    for i in report:
        reporter, reported = i.split()
        idx = id_list.index(reporter)
        tmp[idx].add(reported)

    tmp = list(map(list, tmp))

    # 신고 당한 횟수 체크
    for i in tmp:
        for j in i:
            idx = id_list.index(j)
            cnt_report[idx] += 1
    
    # 내가 신고한 사람이 신수 횟수가 특정 횟수 이상이면 체크
    for i in range(len(id_list)):
        for j in tmp[i]:
            if cnt_report[id_list.index(j)] >= k:
                answer[i] += 1

    return answer

if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    print(solution(id_list, report, k))