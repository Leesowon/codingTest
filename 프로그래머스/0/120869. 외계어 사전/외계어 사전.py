def solution(spell, dic):
    answer = 2
    
    for word in dic :
        cnt = set()
        for w in word :
            if w in spell :
                cnt.add(w)
        
        if len(cnt) == len(spell) :
            answer = 1
            break
    
    return answer