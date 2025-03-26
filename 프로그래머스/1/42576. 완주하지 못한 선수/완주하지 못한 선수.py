def solution(participant, completion):
    answer = ''
    d_part = {}
    for p in participant :
        if p in d_part :
            d_part[p] += 1
        else :
            d_part[p] = 1
    
    for c in completion : 
        d_part[c] -= 1
    
    for d in d_part : 
        if d_part[d] == 1 :
            answer = d
    return answer