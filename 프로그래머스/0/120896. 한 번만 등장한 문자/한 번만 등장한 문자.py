def solution(s):
    answer = ''
    s_set = set(s)
    
    ans = {}
    
    for word in s_set :
        if s.count(word) not in ans :
            ans[s.count(word)] = [word]
        else :
            ans[s.count(word)].append(word)
    
    answer = ''.join(sorted(ans[1]))
    return answer