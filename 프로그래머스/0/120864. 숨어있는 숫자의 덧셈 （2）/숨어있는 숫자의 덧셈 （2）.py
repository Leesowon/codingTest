def solution(my_string):
    answer = 0
    num = ''
    
    for s in my_string :
        if s.isdigit() :
            num += s
        else :
            if num != '' :
                answer += int(num)
                num = ''
                
    if num != '' :
        answer += int(num)
        
    return answer