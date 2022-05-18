def solution(board, moves):
    answer = 0
    basket = []
    for m in moves:
        for b in range(len(board)):
            if board[b][m-1] != 0:
                basket.append(board[b][m-1])
                board[b][m-1] = 0
                break
        if len(basket) >=2 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer += 1
    return answer*2



    return answer

if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))