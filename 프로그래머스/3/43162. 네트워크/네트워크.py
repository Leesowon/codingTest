from collections import deque

# 두 개의 컴퓨터가 연결
# 1번 컴퓨터에 대해 2,3번이 연결되어 있는지 확인 (자기 자신은 제외) : 현재 컴퓨터 기준 더 큰 수의 컴퓨터만 확인하면 됨
# 만약 1번 컴퓨터에 2번 연결 -> 2번 연결된거 다 확인 (깊이 우선 탐색 : dfs - 재귀)
# -> 2번에 3번 연결시, 3번 다 확인
# 3번 다 확인하면 돌아와서 2번 다 확인
# 2번 다 확인하면 1번 다 확인

def solution(n, computers):
    answer = 0
    
    # 확인한 컴퓨터는 더 이상 확인하지 않아도 된다. -> 1차원이면 충분
    visited = [False] * n
    
    def dfs(c) :
        visited[c] = True
        
        for i in range(n):
            if computers[i][c] == 1 and not visited[i] :
                dfs(i)
    
    for i in range(n) :
        if not visited[i]:
            dfs(i) # dfs를 한다는 것 == 연결된 다른 컴퓨터를 못찾았다는 것
            answer += 1       
            
    return answer