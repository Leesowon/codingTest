def solution(n, computers):
    answer = 0
    
    def dfs(node) :
        visited[node] = True
        for next_node in range(n) :
            # 다음 연결 노드에 대해 연결되어있고, 아직 방문하지 않았다면
            if computers[node][next_node] == 1 and not visited[next_node] :
                dfs(next_node)
                
    visited = [False] * n
    
    for i in range(n) :
        if not visited[i] :
            dfs(i)
            answer += 1
    
    return answer