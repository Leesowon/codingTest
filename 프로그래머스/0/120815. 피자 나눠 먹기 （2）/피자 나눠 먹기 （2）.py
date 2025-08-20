import math

def solution(n):
    answer = 0
    # answer은 6과 n의 최소 공배수 // 6
    
    g = math.gcd(n, 6) # 최대 공약수
    
    answer = g * (6//g) * (n//g)
        
    return answer//6