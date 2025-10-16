answer = 0
n = 0
v = []

def dfs(k, cnt, dungeons) :
    global answer
    answer = max(cnt, answer)
    
    for i in range(n) : 
        if k >= dungeons[i][0] and not v[i] :
            v[i] = 1
            dfs(k-dungeons[i][1], cnt+1, dungeons)
            v[i] = 0

def solution(k, dungeons):
    global n, v
    
    n = len(dungeons)
    v = [0] * n
    
    dfs(k, 0, dungeons)
    
    return answer