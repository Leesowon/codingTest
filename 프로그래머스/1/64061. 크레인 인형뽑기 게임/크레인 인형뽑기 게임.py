def solution(board, moves):
    answer = 0
    stack = []
    
    for m in moves :
        for i in range(len(board)) :
            if board[i][m-1] != 0 :
                stack.append(board[i][m-1])
                board[i][m-1] = 0
                
                
                if len(stack) > 1 :
                    d1 = stack.pop()
                    d2 = stack.pop()
                    print('d', d1, d2)

                    if d1 == d2 : # stack이 비어있지 않고, 위에 두개가 같으면
                        answer += 2
                        
                    else :
                        stack.append(d2)
                        stack.append(d1)
                break # 다음 m으로
                
    return answer