import math

def solution(a, b):
    answer = 2
    
    def div(num) :
        if num == 1 :
            return True
        
        if num % 2 == 0 :
            return div(num//2)
        elif num % 5 == 0 :
            return div(num // 5)
        else :
            return False
    
    # 유한소수가 되기 위한 조건 -> 기약분수로 나타내었을 때 분모의 소인수가 2와 5만 존재
    # 기약분수로 만든 법 -> 최대공약수를 구해서, 둘다 최대 공약수로 나누기
    # b // gcd(a,b) 하고 이때의 소인수가 2와 5만 존재해야 한다.
    
    b = b // math.gcd(a,b)
    
    if div(b) :
        answer = 1
    
    return answer