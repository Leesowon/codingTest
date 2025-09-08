def solution(my_string):
    answer = 0
    operation = ['+', '-']
    
    li = list(my_string.split(' '))
    
    num = []
    oper = []
    
    for value in li :
        if value not in operation :
            num.append(int(value))
        else :
            oper.append(value)
    
    answer = num.pop(0)
    
    while oper :
        op = oper.pop(0)
        n = num.pop(0)
        
        if op == '+' :
            answer += n
        else :
            answer -= n
    return answer