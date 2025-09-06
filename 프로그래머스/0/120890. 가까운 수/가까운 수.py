def solution(array, n):
    answer = array[0]
    
    for arr in array :
        if abs(n-arr) < abs(answer-n) :
            answer = arr
        elif abs(n-arr) == abs(answer-n) :
            answer = min(answer, arr)
            
    return answer