def solution(n):
    number = [1, 2, 4]
    answer = ''
    while n>0 :
        if n % 3 == 0:
            answer += '4'
            n = n // 3 - 1
        else:
            answer += str(number[n%3 -1])
            n //= 3

    return answer[::-1]

if __name__ == '__main__':
    n = 15
    print(solution(n))
