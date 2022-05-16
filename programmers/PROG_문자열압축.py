def solution(s):
    answer = 10000
    # i:비교할 문자열의 개수
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        res = ''
        hit = 1
        tmp = s[:i]
        for j in range(i, len(s)+i, i):
            if tmp == s[j:j+i]:
                hit += 1
            else:
                if hit == 1:
                    res += tmp
                else:
                    res += str(hit) + tmp
                tmp = s[j:j+i]
                hit = 1

        answer = min(answer, len(res))

    return answer

if __name__ == '__main__':
    print(solution("a"))