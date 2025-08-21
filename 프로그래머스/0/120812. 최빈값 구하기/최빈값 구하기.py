def solution(array):
    answer = [0] * 1001
    for arr in array :
        answer[arr] += 1
    
    if answer.count(max(answer)) > 1:
        return -1
    
    ans = answer.index(max(answer))
    return ans