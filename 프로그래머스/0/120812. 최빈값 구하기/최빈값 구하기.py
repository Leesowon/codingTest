def solution(array):
    answer = [0] * 1000
    
    for arr in array :
        answer[arr] += 1
    
    if answer.count(max(answer)) > 1 :
        return -1
    
    return answer.index(max(answer))