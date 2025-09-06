def solution(order):
    answer = 0
    
    for o in str(order) :
        if o in '369' : 
            answer += 1
    return answer