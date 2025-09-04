def solution(my_string):
    answer = ''
    my_str = set(list(my_string))
    
    for s in my_string :
        if s not in answer :
            answer += s
    
    return answer