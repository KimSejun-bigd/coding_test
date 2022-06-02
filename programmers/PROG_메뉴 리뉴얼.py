import itertools
from collections import Counter

def solution(orders, course):
    for i in range(len(orders)):
        orders[i] = "".join(list(sorted(orders[i])))
    # print(orders)
    answer = []
    tmp_list_max = [[] for _ in range(max(course))]
    # print(tmp_list_max)
    tmp_list = set([])  #음식 조합이 들어갈 리스트

    for c in course:
        if c >= len(orders):
            break
        for i in range(len(orders)):
            combi = list(itertools.combinations(orders[i], c))
            for com in combi:
                tmp_list.add(com)

    tmp_list = sorted(list(tmp_list), key=lambda x: len(x))
    # cnt = [0] * len(tmp_list)
    cnt = []
    for i in orders:
        for j in tmp_list:
            for k in j:
                if k not in i:
                    break;
            else:
                # print(j)
                # cnt[tmp_list.index(j)] += 1
                cnt.append(j)
                # tmp_list_max[len(j)-1].append("".join(j))
    # print(tmp_list_max)
    counter = Counter(cnt)
    counter = list(counter.most_common())
    counter.sort(key=lambda x: (len(x[0]), -x[1]))

    print(counter)

    for c in range(len(course)):
        max_cnt = 0
        for i in range(len(counter)):
            if course[c] != len(counter[i][0]) and c < len(course)-1:
                c += 1
            if course[c] == len(counter[i][0]) and max_cnt <= counter[i][1] :
                max_cnt = counter[i][1]
                answer.append("".join(counter[i][0]))

    return answer

if __name__ == '__main__':
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    print(solution(orders, course))