def solution(keyinput, board):
    answer = []
    
    r, c = 0, 0
    w = board[0]
    h = board[1]
    
    for move in keyinput :
        if move == "left" and (r-1) >= -(w//2) :
            r -= 1
        elif move == "right" and (r+1) <= w//2 :
            r += 1
        elif move == "down" and (c-1) >= -(h//2) :
            c -= 1
        elif move == "up" and (c+1) <= h//2 :
            c += 1
    
    return [r,c]