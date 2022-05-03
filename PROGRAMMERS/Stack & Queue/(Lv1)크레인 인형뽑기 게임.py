def solution(board, moves):
    answer = 0
    N = len(board)
    s = []
    for j in moves:
        i = 0
        flag = True
        while board[i][j - 1] == 0:
            i += 1
            if i == N:
                flag = False
                break
        if flag:            
            p = board[i][j - 1]
            board[i][j - 1] = 0
            if not s:
                s.append(p)
            elif p != s[-1]:
                s.append(p)
            else:
                s.pop()
                answer += 2    
    return answer
