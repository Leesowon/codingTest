def solution(prices):
    answer = [0] * len(prices)
    stack = [] # 아직 떨어지지 않은 주식가격에 대한 인덱스
    
    for i in range(len(prices)) :
        while stack and prices[i] < prices[stack[-1]] :
            idx = stack.pop()
            answer[idx] = i-idx
        stack.append(i)
        
    if len(stack) > 0 :
        for j in stack :
            answer[j] = (len(prices) - j - 1)
    
    return answer