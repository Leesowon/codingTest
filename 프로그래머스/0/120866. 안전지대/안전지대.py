def solution(board):
    answer = 0
    
    dh = [-1, -1, -1, 0, 0, 1, 1, 1]
    dw = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for i in range(len(board)) :
        for j in range(len(board[0])) :
            
            if board[i][j] != 1 :
                bomb = False
                for k in range(8) :
                    nh = i + dh[k]
                    nw = j + dw[k]
                    
                    if 0 <= nh < len(board) and 0 <= nw < len(board[0]) :
                        if board[nh][nw] == 1 :
                            bomb = True
                            break
                    
                if not bomb :
                    answer += 1
            
    
    return answer