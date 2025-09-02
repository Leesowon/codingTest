import math 

def solution(n):
    answer = 0
    
    for i in range (1, 12) :
        if math.factorial(i) > n :
            answer = i-1
            break
    # print(math.factorial(3))
    
    return answer