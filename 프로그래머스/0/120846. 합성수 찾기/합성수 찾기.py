def solution(n):
    
    answer = 0
    
    for i in range(2, n+1) : 
        if isHap(i) :
            answer += 1
            
    return answer

def isHap(num) :
        cnt = 1
        for i in range(2, num+1) : 
            if num % i == 0 :
                cnt += 1
        if cnt >= 3 :
            return True
        return False