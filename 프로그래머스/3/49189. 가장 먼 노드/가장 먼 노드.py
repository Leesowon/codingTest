from collections import deque

def solution(n, edge):
    answer = 0
    
    # 연결된 노드 정보 그래프
    g = [[] for _ in range(n+1)]
    distance = [-1] * (n+1)
    
    for e in edge :
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])
    
    d = deque([1]) # 출발 노드 1
    distance[1] = 0
    
    while d :
        now = d.popleft()
        
        for node in g[now] : # 현재 노드에서 이동할 수 있는 노드
            if distance[node] == -1 : # 아직 방문하지 않았다면
                d.append(node)
                distance[node] = distance[now] + 1
    
    answer = distance.count(max(distance))
    
    return answer