def solution(name):
    answer = 0
    
    n = len(name)
    
    # 상하 최소 이동
    for word in name :
        answer += min((ord(word)-ord('A')), (ord('Z')-ord(word)+1))
    
    move = n-1
    for i in range(n) :
        next_idx = i+1
        while next_idx < n and name[next_idx] == 'A' : # 최대 연속 A 찾기
            next_idx += 1
        move = min(move, i+n-next_idx + min(i, n-next_idx))
    
    answer += move
        
    return answer