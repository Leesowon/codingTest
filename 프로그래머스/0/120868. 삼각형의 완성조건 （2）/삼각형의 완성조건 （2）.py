def solution(sides):
    answer = 0
    
    a = max(sides)
    b = min(sides)
    
    answer += b
    answer += b-1
        
    return answer