def solution(s):
    answer = True
    stack = []
    
    for g in s :
        if g == "(" :
            stack.append("(")
        else : 
            if len(stack)>0 and stack[-1] == "(" :
                stack.pop()
            else :
                stack.append(g)
                
    if len(stack) > 0 :
        answer = False
    
    return answer