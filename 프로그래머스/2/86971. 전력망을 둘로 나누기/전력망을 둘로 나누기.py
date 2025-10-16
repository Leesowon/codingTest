visited = []

def dfs(node, ck_wires) :
    
    visited[node] = 1
    cnt = 1

    for a,b in ck_wires:
        if a == node and not visited[b] :
            cnt += dfs(b, ck_wires)
        elif b == node and not visited[a] :
            cnt += dfs(a, ck_wires)
    return cnt

def solution(n, wires):
    global visited
    answer = float('inf')
    
    for i in range(len(wires)) :
        ck_wires = wires[:i] + wires[i+1:]
        
        visited = [0] * (n+1)
        a, b = ck_wires[0]
        
        cnt = dfs(a, ck_wires)
        diff = abs(n- 2*cnt) # cnt - (n-cnt) = n - 2*cnt
        answer = min(answer, diff)
    
    return answer