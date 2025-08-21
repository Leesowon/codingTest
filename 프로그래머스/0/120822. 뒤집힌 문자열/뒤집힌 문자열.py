def solution(my_string):
    answer = ''
    li = list(my_string)[::-1]
    
    return answer.join(map(str, li))