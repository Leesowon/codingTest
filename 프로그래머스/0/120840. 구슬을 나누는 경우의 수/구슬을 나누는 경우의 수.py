def solution(balls, share):
    answer = 0
    
    # n! / r!(n-r)!
    
    # n! == balls
    n = 1
    for i in range(2, balls+1) :
        n *= i
    
    # r!
    r = 1
    for i in range(2, share+1) : 
        r *= i
    
    # (n-r)!
    nr = 1
    for i in range(2, (balls-share)+1) :
        nr *= i
    
    answer = n / (r*nr)
        
    return answer