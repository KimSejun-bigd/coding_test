def solution(s):
    result = s
    numstr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for j in range(len(numstr)):
        if numstr[j] in s:
            result = result.replace(numstr[j], str(j), )
    return int(result)

if __name__ == '__main__':
    s = 'one4seveneight'
    print(solution(s))