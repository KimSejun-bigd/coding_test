def solution(numbers, hand):

    keypad = {'1':[0,0], '2':[0,1], '3':[0,2], '4':[1,0], '5':[1,1], '6':[1,2], '7':[2,0], '8':[2,1], '9':[2,2], '*':[3,0], '0':[3,1], '#':[3,2]}
    answer = ''

    left = '*'
    right = '#'
    for i in numbers:

        if i in (1,4,7):
            answer += "L"
            left = str(i)
        elif i in (3,6,9):
            answer += "R"
            right = str(i)
        else:
            #왼/오른손으로 움직일때 거리 계산(keypad dictionary에 저장해둔 x,y 좌표를 가지고 절대값 계산하여 거리 계산)
            dx_left = abs(keypad[left][0] - keypad[str(i)][0]) +abs(keypad[left][1] - keypad[str(i)][1])
            dx_right = abs(keypad[right][0] - keypad[str(i)][0]) + abs(keypad[right][1] - keypad[str(i)][1])

            #왼손 거리 > 오른손 거리
            if dx_left > dx_right:
                answer += 'R'
                right = str(i)

            # 왼손 거리 , 오른손 거리
            elif dx_left < dx_right:
                answer += 'L'
                left = str(i)

            # 왼손 거리 = 오른손 거리:hand 매개변수에 따라서
            else:
                if hand == 'right':
                    answer += 'R'
                    right = str(i)
                else:
                    answer += 'L'
                    left = str(i)

    return answer

if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"

    print(solution(numbers, hand))